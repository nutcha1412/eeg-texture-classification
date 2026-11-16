# EEG Dataset Documentation
This folder documents the structure of the EEG data used in the
texture-classification project. The original participant recordings
are not included in this public repository. The only CSV example
intended for publication is synthetic_eeg_training_sample.csv, which
contains fabricated values for demonstrating the model-input schema.

## 1. Data collection overview
EEG recordings were collected during experiments involving four
recording conditions/classes represented in the supplied raw-file
examples:
- Normal
- Flat
- Furry
- Rough
The acquisition scripts save raw recordings as .txt files. The
supplied examples use filenames such as 8channelsFlatR.txt and
8channelsNormalR.txt

### Raw .txt file structure
The supplied raw .txt examples are comma-separated text files with
11 columns:

<img width="472" height="423" alt="image" src="https://github.com/user-attachments/assets/96e10294-ed1c-42e3-aff1-cb6fcf473b87" />

| Column | Description |
|---|---|
| index | Sequential sample/row index |
| Pz | EEG channel Pz |
| P1 | EEG channel P1 |
| P3 | EEG channel P3 |
| P5 | EEG channel P5 |
| CPz | EEG channel CPz |
| CP1 | EEG channel CP1 |
| CP3 | EEG channel CP3 |
| CP5 | EEG channel CP5 |
| timestamp | Recording timestamp |
| timeFormat | Human-readable time string |

Each row represents one recorded sample. The eight EEG channel columns
contain the recorded signal values; timestamp and timeFormat provide
timing information.

Left/right channel note: the processed training table described
below contains four left-side channels (P3, P5, CP3, CP5) and
four right-side channels (P4, P6, CP4, CP6). However, the raw
.txt examples supplied for documentation contain Pz, P1, P3,
P5, CPz, CP1, CP3, and CP5---they do not show the right-side
P4, P6, CP4, and CP6 columns. Confirm the acquisition script's
left/right recording arrangement and any channel-mapping or merging step
before claiming that each raw .txt file contains both hemispheres.
Keep the original left/right recordings in their original form; do not
discard either side.

## 2. Processed training data (.csv)
The processed model-input table uses 41 columns:
- 40 numerical feature columns: five frequency-band features for
  each of eight EEG channels.
- 1 target column: Label, containing the texture class.

### Channel groups
The eight channels are:
- Left side: P3, P5, CP3, CP5
- Right side: P4, P6, CP4, CP6

### Feature naming convention
Each feature name is formed by joining the frequency-band name and
channel name, for example DeltaP3 or GammaCP6.

The five frequency bands are:
- Delta
- Theta
- Alpha
- Beta
- Gamma

### Complete CSV column order
1. DeltaP3, ThetaP3, AlphaP3, BetaP3, GammaP3
2. DeltaP5, ThetaP5, AlphaP5, BetaP5, GammaP5
3. DeltaCP3, ThetaCP3, AlphaCP3, BetaCP3, GammaCP3
4. DeltaCP5, ThetaCP5, AlphaCP5, BetaCP5, GammaCP5
5. DeltaP4, ThetaP4, AlphaP4, BetaP4, GammaP4
6. DeltaP6, ThetaP6, AlphaP6, BetaP6, GammaP6
7. DeltaCP4, ThetaCP4, AlphaCP4, BetaCP4, GammaCP4
8. DeltaCP6, ThetaCP6, AlphaCP6, BetaCP6, GammaCP6
9. Label
The supplied dataset_part1.csv has 360 rows and 41 columns, with
120 rows for each label: flat, furry, and rough. This describes
that supplied processed file; it should not be interpreted as the total
number of raw EEG samples or participants.

## 3. Raw-to-processed data workflow
The project data flow can be documented at this level:
1. Recording: acquisition scripts record EEG signals and save raw
   channel values and timing information in .txt files.
2. Loading: the recorded files are loaded for analysis.
3. Preprocessing: the signals are prepared for feature analysis.
   Refer to the project notebooks for the exact filtering,
   segmentation, and cleaning operations.
4. Frequency analysis / feature extraction: frequency-band features
   are calculated for the eight channels. The processed feature table
   uses the five band names Delta, Theta, Alpha, Beta, and
   Gamma.
5. Label assignment: each feature row receives a Label
   identifying the corresponding class (flat, furry, or rough).
6. Model input: the resulting CSV contains 40 numeric features plus
   the target label and is used as the input table for model
   training/validation.
The exact filter settings, frequency cut-offs, window length, overlap,
normalization method, and aggregation method are not specified here. Add
those parameters only after verifying them against the preprocessing and
training notebooks; they should not be inferred from the column names
alone.

## 4. Public sample file
synthetic_eeg_training_sample.csv is a small synthetic demonstration
file with:
- 9 rows (3 examples per class)
- 40 numeric feature columns
- 1 Label column
- Labels: flat, furry, and rough
All values in this sample were generated artificially to demonstrate the
expected CSV layout. They are not real EEG recordings, are not copied
rows from the collected dataset, and must not be used to reproduce or
evaluate the research results.

## 5. Privacy and repository policy
- Do not upload original participant-level .txt recordings or real
  processed participant-level CSV files to this public repository
  unless the required consent and approvals explicitly permit public
  release.
- Do not publish participant identifiers, identifiable timestamps, or
  other information that could reveal a participant's identity.
- Keep private raw data and any files containing participant-level
  information outside the public repository.
- Use the synthetic CSV only to demonstrate the feature schema and
  expected model-input format.

## Folder layout
data/

├── README.md

└── synthetic_eeg_training_sample.csv
