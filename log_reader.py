import pickle

with open("log_file.bin","rb") as f:
    data = pickle.load(f);
    print(data)
