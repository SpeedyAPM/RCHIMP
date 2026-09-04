# BassDetector Experimental Evaluation Workflow

## Aktualny stan kodu przed zmianami

### Android

- Audio jest pobierane z mikrofonu przez `AudioRecord` z `MediaRecorder.AudioSource.MIC`.
- Konfiguracja wejścia jest zdefiniowana w `app/src/main/res/values/config.xml`:
  - `sample_rate_hz = 22050`
  - `fft_size = 2048`
  - `hop_length = 512`
  - `bass_threshold = 106.0`
- `AudioRecord` działa w `CHANNEL_IN_MONO` i `ENCODING_PCM_FLOAT`.
- Odczyt audio i analiza działały w korutynie `Dispatchers.Default` w `BassDetectorEngine`.
- UI i sygnalizacja były wykonywane na `Dispatchers.Main` i dodatkowo przez `runOnUiThread` w `MainActivity`.
- Wykrywanie basu było realizowane przez `BassAnalyzer`, który utrzymywał przesuwne okno FFT i wybierał najsilniejszą składową poniżej `maxBassFrequency`.
- Debounce opierał się wcześniej na `System.currentTimeMillis()`, więc nie było spójnego mapowania do osi czasu audio.
- Projekt nie miał trwałego logu zdarzeń, pliku WAV, metadanych sesji ani eksportu danych porównawczych.

### BeatNet

- Repozytorium referencyjne znajduje się w `BeatNet/`.
- README BeatNet deklaruje tryby `stream`, `realtime`, `online`, `offline`.
- Dla wejścia plikowego BeatNet sam resampluje do `22050 Hz`; dla wejścia jako obiekt audio oczekuje `22050 Hz`.
- Zwracany wynik ma postać tablicy `numpy_array(num_beats, 2)`, gdzie kolumny oznaczają:
  - czas zdarzenia w sekundach
  - pozycję w takcie używaną do rozróżnienia beat/downbeat
- W Androidzie wrapper BeatNet był wcześniej tylko częściową integracją i nie produkował trwałych artefaktów badawczych.

## Co zostało dodane

### Android

- `ExperimentalSession`, `ExperimentalSessionManager`:
  - generowanie `session_id`
  - katalog sesji
  - zapis `session_metadata.json`
- `DetectorEventRecord`:
  - stabilny format logu zdarzeń w `events.jsonl`
  - rozróżnienie `bass_onset`, `beat`, `downbeat`, `tempo_update`, `ui_signal`, `diagnostic`
- `AudioTimelineMapper`:
  - mapowanie `audio_frame <-> audio_time_sec`
  - wyliczanie początku, środka i końca okna analitycznego
  - estymacja opóźnienia względem czasu monotonicznego
- `AsyncFloatWavWriter`:
  - nieblokujący zapis `input.wav`
  - kolejka producent-konsument
  - finalizacja nagłówka WAV
  - raportowanie przepełnienia kolejki i błędów zapisu
- `BassDetectorEngine`:
  - logowanie zdarzeń algorytmicznych przed sygnałem do UI
  - zapis bloków audio do kolejki WAV
  - logowanie zdarzeń BeatNet i `tempo_update`
  - start/stop sesji eksperymentalnej
- `MainActivity`:
  - integracja z `ExperimentalSessionManager`
  - pokazywanie `session_id` i ścieżki metadanych po zatrzymaniu

### Python

- `tools/run_beatnet_offline.py`:
  - uruchamia lokalny BeatNet z repozytorium
  - zapisuje wynik do JSONL
  - opcjonalnie zapisuje CSV
  - zapisuje metadane wykonania do JSON
- `tools/compare_android_to_beatnet.py`:
  - wczytuje log Androida i wyniki BeatNet
  - wspiera wspólną oś czasu przez WAV
  - opcjonalnie estymuje offset korelacją krzyżową
  - opcjonalnie dopasowuje liniowy drift `t_ref = a * t_android + b`
  - opcjonalnie wykrywa marker synchronizacyjny
  - wykonuje dopasowanie one-to-one
  - zapisuje raport i tabele wynikowe

## Artefakty sesji Android

Każda sesja tworzy katalog w:

```text
<filesDir>/experimental_sessions/<session_id>/
```

Pliki:

- `<session_id>_session_metadata.json`
- `<session_id>_events.jsonl`
- `<session_id>_input.wav`

### `events.jsonl`

Rekordy zawierają zależnie od typu zdarzenia między innymi:

- `session_id`
- `event_id`
- `event_type`
- `audio_frame`
- `audio_time_sec`
- `sample_rate_hz`
- `block_start_frame`
- `block_end_frame_exclusive`
- `analysis_window_start_frame`
- `analysis_window_center_frame`
- `analysis_window_end_frame_exclusive`
- `decision_time_monotonic_ns`
- `ui_dispatch_time_monotonic_ns`
- `estimated_capture_monotonic_ns`
- `detection_latency_ms`
- `confidence`
- `bpm`
- `frequency_hz`
- `magnitude`
- `config_id`

## Workflow eksperymentu

1. Uruchom aplikację Android.
2. Rozpocznij sesję przyciskiem start.
3. Odtwórz materiał testowy, opcjonalnie z markerem synchronizacyjnym.
4. Zatrzymaj sesję.
5. Skopiuj `input.wav`, `events.jsonl` i `session_metadata.json` na komputer.
6. Uruchom BeatNet offline na zapisanym WAV.
7. Uruchom porównanie logu Androida z wynikami BeatNet.
8. Odczytaj `summary.json` i tabele CSV.

## Przykładowe polecenia

### BeatNet offline

```powershell
& "C:\Users\wojte\AppData\Local\Programs\Python\Python38\python.exe" `
  "tools/run_beatnet_offline.py" `
  --input-wav "C:\path\to\input.wav" `
  --mode offline `
  --output-jsonl "C:\path\to\beatnet_events.jsonl" `
  --output-csv "C:\path\to\beatnet_events.csv" `
  --metadata-json "C:\path\to\beatnet_metadata.json"
```

### Porównanie Android vs BeatNet

```powershell
& "C:\Users\wojte\AppData\Local\Programs\Python\Python38\python.exe" `
  "tools/compare_android_to_beatnet.py" `
  --android-log "C:\path\to\events.jsonl" `
  --session-metadata "C:\path\to\session_metadata.json" `
  --beatnet-results "C:\path\to\beatnet_events.jsonl" `
  --beatnet-metadata "C:\path\to\beatnet_metadata.json" `
  --wav "C:\path\to\input.wav" `
  --android-event-types "beat,downbeat" `
  --reference-event-types "beat,downbeat" `
  --tolerances-ms 20,30,50,70,100 `
  --estimate-offset `
  --fit-linear-drift `
  --detect-sync-marker `
  --output-dir "C:\path\to\comparison"
```

## Jak interpretować porównanie

- `BeatNet offline` jest referencją nieprzyczynową, więc zwykle będzie korzystniejszy niż algorytm realtime.
- `bass_onset` z Androida nie jest tym samym co `beat` lub `downbeat` z BeatNet.
- Uczciwe porównania to przede wszystkim:
  - Android `beat` vs BeatNet `beat`
  - Android `downbeat` vs BeatNet `downbeat`
  - osobna analiza `bass_onset`
- Offset i drift pomagają zsynchronizować osie czasu, ale nie powinny ukrywać rzeczywistych błędów algorytmu.

## Ograniczenia

- Androidowy wrapper BeatNet jest nadal ścieżką eksperymentalną i nie powinien być traktowany jako lekki kod realtime.
- Lokalne uruchomienie skryptów BeatNet wymaga środowiska Pythona z `numpy`, `scipy`, `librosa`, `torch` oraz lokalnymi źródłami BeatNet/madmom.
- Porównanie z BeatNet offline nie odpowiada dokładnie sytuacji przyczynowej w czasie rzeczywistym.
- Jeżeli Android loguje głównie zdarzenia basowe, do oceny tych zdarzeń warto przygotować osobną referencję `bass_onset`.
