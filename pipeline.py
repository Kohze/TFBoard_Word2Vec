import os.path
import argparse
import sys
import subprocess
import webbrowser
import os
import signal

parser = argparse.ArgumentParser(description='The pipeline script to learn word embeddings and visualize them via tensorboard.')

parser.add_argument('--word2vec_path', 
                    default='./word2vec.py',
                    help='Path to the word2vec script')

parser.add_argument('--tensorboard_path', 
                    default='tensorboard',
                    help='Path to the tensorboard')

parser.add_argument('--tensorboard_port', 
                    default='6010',
                    help='Port to the tensorboard')

#word2vec arguments
parser.add_argument('--save_path', 
                    help='Directory to write the model and training summaries.')

parser.add_argument('--train_data', 
                    help='Training text file. E.g., unzipped file http://mattmahoney.net/dc/text8.zip.')

parser.add_argument('--eval_data', 
                    help='File consisting of analogies of four tokens embedding 2 - embedding 1 + embedding 3 should be close to embedding 4. See README.md for how to get \'questions-words.txt\'.')

parser.add_argument('--embedding_size', 
                    default='200',
                    help='The embedding dimension size.')

parser.add_argument('--epochs_to_train', 
                    default='15',
                    help='Number of epochs to train. Each epoch processes the training data once completely.')

parser.add_argument('--learning_rate', 
                    default='0.2',
                    help='Initial learning rate.')

parser.add_argument('--num_neg_samples', 
                    default='100',
                    help='Negative samples per training example.')

parser.add_argument('--batch_size', 
                    default='16',
                    help='Number of training examples processed per step (size of a minibatch).')

parser.add_argument('--concurrent_steps', 
                    default='12',
                    help='The number of concurrent training steps.')

parser.add_argument('--window_size', 
                    default='5',
                    help='The number of words to predict to the left and right of the target word.')

parser.add_argument('--min_count', 
                    default='5',
                    help='The minimum number of word occurrences for it to be included in the vocabulary.')

parser.add_argument('--subsample',
                    default='1e-3',
                    help='Subsample threshold for word occurrence. Words that appear with higher frequency will be randomly down-sampled. Set to 0 to disable.')

parser.add_argument('--interactive', 
                    default='False',
                    help="If true, enters an IPython interactive session to play with the trained model. E.g., try model.analogy(b'france', b'paris', b'russia') and model.nearby([b'proton', b'elephant', b'maxwell'])")

parser.add_argument('--statistics_interval', 
                    default='5',
                    help='Print statistics every n seconds.')

parser.add_argument('--summary_interval', 
                    default='5',
                    help="Save training summary to file every n seconds (rounded up to statistics interval).")

parser.add_argument('--checkpoint_interval', 
                    default='600',
                    help="Checkpoint the model (i.e. save the parameters) every n seconds (rounded up to statistics interval).")

arg = parser.parse_args(sys.argv[1:])
print(arg)

if not os.path.isfile(arg.word2vec_path):
    raise Exception('The script word2vec.py is not found.')

if os.path.exists(arg.save_path):
    for f in os.listdir(arg.save_path):
        os.remove(os.path.join(arg.save_path, f))

if os.path.isfile('pipeline.pid'):
    f = open('pipeline.pid', 'r')
    pid = f.read()
    print("Previous tensorboard PID: "+str(pid))
    f.close()
    try:
        os.kill(int(pid), signal.SIGTERM)
    except:
        pass

subprocess.call(["python", arg.word2vec_path,   "--save_path", arg.save_path,
                                                "--train_data", arg.train_data,
                                                "--eval_data", arg.eval_data,
                                                "--embedding_size", arg.embedding_size,
                                                "--epochs_to_train", arg.epochs_to_train,
                                                "--learning_rate", arg.learning_rate,
                                                "--num_neg_samples", arg.num_neg_samples,
                                                "--batch_size", arg.batch_size,
                                                "--concurrent_steps", arg.concurrent_steps,
                                                "--window_size", arg.window_size,
                                                "--min_count", arg.min_count,
                                                "--subsample", arg.subsample,
                                                "--interactive", arg.interactive,
                                                "--statistics_interval", arg.statistics_interval,
                                                "--summary_interval", arg.summary_interval,
                                                "--checkpoint_interval", arg.checkpoint_interval ])

proc = subprocess.Popen(["tensorboard", "--logdir="+arg.save_path, "--port="+str(arg.tensorboard_port)])

print("PID:"+str(proc.pid))
f = open('pipeline.pid', 'w')
f.write(str(proc.pid))
f.close()

webbrowser.open("http://127.0.0.1:"+str(arg.tensorboard_port))
