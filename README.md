## Drug Target Interaction
#### Goal
* [Drug repurposing] Drug - Target binding affinity score prediction

#### Method
1. Drug encoder, Target encoder specification
2. Data encoding and split
3. Model configuration Generation (parameter)
4. Model Initialization
5. Model Training
6. Model Prediction and Repurposing
7. Model Saving and Loading

#### Data
1. [BindingDB](https://www.bindingdb.org/bind/index.jsp)
2. [DAVIS](http://staff.cs.utu.fi/~aatapa/data/DrugTarget/)
3. [KIBA](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-017-0209-z)

#### File Structure
```bash
├── DeepPurpose
│   ├── DTI.py
│   ├── encoders.py
│   ├── model_helper.py
│   ├── oneliner.py
│   ├── utils.py
│   └── dataset.py
├── save_folder
│   └── pretrained_models
└── data
``` 
#### Input / Output example
```
----input----
Drug1_SMILES Drug1_Name Target1_Seq Target1_Name
Drug1_SMILES Drug1_Name Target1_Seq Target1_Name
```
```
----output----
Drug Repurposing Result for SARS-CoV2 3CL Protease
+------+----------------------+------------------------+---------------+
| Rank |      Drug Name       |      Target Name       | Binding Score |
+------+----------------------+------------------------+---------------+
|  1   |      Sofosbuvir      | SARS-CoV2 3CL Protease |     190.25    |
|  2   |     Daclatasvir      | SARS-CoV2 3CL Protease |     214.58    |
|  3   |      Vicriviroc      | SARS-CoV2 3CL Protease |     315.70    |
|  4   |      Simeprevir      | SARS-CoV2 3CL Protease |     396.53    |
|  5   |      Etravirine      | SARS-CoV2 3CL Protease |     409.34    |
|  6   |      Amantadine      | SARS-CoV2 3CL Protease |     419.76    |
|  7   |      Letermovir      | SARS-CoV2 3CL Protease |     460.28    |
|  8   |     Rilpivirine      | SARS-CoV2 3CL Protease |     470.79    |
|  9   |      Darunavir       | SARS-CoV2 3CL Protease |     472.24    |
|  10  |      Lopinavir       | SARS-CoV2 3CL Protease |     473.01    |
|  11  |      Maraviroc       | SARS-CoV2 3CL Protease |     474.86    |
|  12  |    Fosamprenavir     | SARS-CoV2 3CL Protease |     487.45    |
|  13  |      Ritonavir       | SARS-CoV2 3CL Protease |     492.19    |
....
```

## TFBS Data Analysis
#### Goal
* Transcription Factor Binding Site Data preprocessing
* Reduce Time consumption using multiprocessing in Dataframe 

#### Data
1. Chromosome Transcription Factor Binding Site DB
2. DNA sequence Data
3. Oncogene Data
4. Tumor Suppressor gene Data

#### Preprocessing (ver1)
1. Add DNA sequence data (using RestAPI or fasta file, multiprocessing)
2. Split Dataframe column (using explode, str.split)
3. Edit DNA sequence to reverse complement sequence (using Biopython, multiprocessing)

#### Mapping with promoter sequence data, Oncogene data, Tumor Suppressor Gene data (ver2)
1. Compute SmithWaterman Score between promoter sequence and TFBS sequence (using skbio.alignment, multiprocessing)
2. Compute Mismatch Score between promoter sequence and TFBS sequence (using multiprocessing)
3. Check oncogene, tumor suppressor gene in TFBS data (using multiprocessing)

## Pathway Database
#### Goal
* STRING Pathway Database(PostgreSQL Database dump file) Annotation

#### Database Table
1. actions table
2. proteins table
3. sets table
4. sets_items table 

#### Method Step
1. Protein id -> Protein name (Join actions Table & proteins Table)
2. Specify comment of pathway (Join sets Table & sets_items Table)
3. Join result data of step 1, step 2

## Gene Variant Check
#### Data
1. NCBI clinvar Data (variant information)
2. Gene Sequence Data

#### Goal
* Check gene variant location

## Multiprocessing mapping
* Application of Multiprocessing