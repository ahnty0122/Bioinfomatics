from DeepPurpose import utils, dataset
from DeepPurpose import DTI as models
import warnings
warnings.filterwarnings("ignore")

X_drugs, X_targets, y = dataset.load_process_KIBA(path = './data', binary = False, threshold = 9)

drug_encoding, target_encoding = 'Transformer', 'CNN'

train, val, test = utils.data_process(X_drugs, X_targets, y, 
                                drug_encoding, target_encoding, 
                                split_method='random',frac=[0.7,0.1,0.2],
                                random_seed = 1)

config = utils.generate_config(drug_encoding = drug_encoding, target_encoding = target_encoding, 
					result_folder = "./result/",
					input_dim_drug = 1024, 
					input_dim_protein = 8420,
					hidden_dim_drug = 256, 
					hidden_dim_protein = 256,
					cls_hidden_dims = [1024, 1024, 512],
					mlp_hidden_dims_drug = [1024, 256, 64],
					mlp_hidden_dims_target = [1024, 256, 64],
					batch_size = 256,
					train_epoch = 100,
					test_every_X_epoch = 20,
					LR = 1e-4,
					decay = 0,
					transformer_emb_size_drug = 128,
					transformer_intermediate_size_drug = 512,
					transformer_num_attention_heads_drug = 8,
					transformer_n_layer_drug = 8,
					transformer_emb_size_target = 64,
					transformer_intermediate_size_target = 256,
					transformer_num_attention_heads_target = 4,
					transformer_n_layer_target = 2,
					transformer_dropout_rate = 0.1,
					transformer_attention_probs_dropout = 0.1,
					transformer_hidden_dropout_rate = 0.1,
					mpnn_hidden_size = 50,
					mpnn_depth = 3,
					cnn_drug_filters = [32,64,96],
					cnn_drug_kernels = [4,6,8],
					cnn_target_filters = [32,64,96],
					cnn_target_kernels = [4,8,12],
					rnn_Use_GRU_LSTM_drug = 'GRU',
					rnn_drug_hid_dim = 64,
					rnn_drug_n_layers = 2,
					rnn_drug_bidirectional = True,
					rnn_Use_GRU_LSTM_target = 'GRU',
					rnn_target_hid_dim = 64,
					rnn_target_n_layers = 2,
					rnn_target_bidirectional = True,
					num_workers = 0)


model = models.model_initialize(**config)

model.train(train, val, test)

model.save_model('./tutorial_model')