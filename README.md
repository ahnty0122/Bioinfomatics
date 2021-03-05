## _1. TFBS Data Analysis_
#### Goal
* Transcription Factor Binding Site Data preprocessing
* Reduce Time consumption using multiprocessing in Dataframe 

#### Data
* private

#### Preprocessing
* using RestAPI, multiprocessing
* Split Dataframe column (using explode, str.split)
* Edit DNA sequence to reverse complement sequence (using Biopython, multiprocessing)

#### Mapping with other data
* private

## _2. Pathway Database_
#### Goal
* STRING Pathway Database(__PostgreSQL Database dump file__) Annotation

#### Database Schema
<img src="https://user-images.githubusercontent.com/61795757/110055854-19251780-7da1-11eb-8805-1c892431b2cc.PNG" width="70%" height="80%"/>

#### Using Table
* network.actions table
* items.proteins table
* evidence.sets table
* evidence.sets_items table 

#### Method Step
* Protein id -> Protein name (Join actions Table & proteins Table)
* Specify comment of pathway (Join sets Table & sets_items Table)
* Join result data of step 1, step 2  


## _3. Gene Variant Check_
#### Data
* NCBI clinvar Data (variant information)
* Gene Sequence Data

#### Goal
* Check gene variant location  


## _4. Multiprocessing mapping_
* Application of Multiprocessing  


## _5. Drug Target Interaction_
#### Goal
* __[Drug repurposing]__ Drug - Target binding affinity score prediction

#### Method
* Drug encoder, Target encoder specification
* Data encoding and split
* Model configuration Generation (parameter)
* Model Initialization
* Model Training
* Model Prediction and Repurposing
* Model Saving and Loading

#### Data
* [BindingDB](https://www.bindingdb.org/bind/index.jsp)
* [DAVIS](http://staff.cs.utu.fi/~aatapa/data/DrugTarget/)
* [KIBA](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-017-0209-z)

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
