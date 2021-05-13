import pickle
with (open("athal_reaction_to_SK1.pkl", "rb")) as openfile:
    while True:
        try:
            X_train, y_train, X_test, y_test = pickle.load(openfile)
            print(X_train)
            print(y_train)
            print(X_test)
            print(y_test)
        except EOFError:
            break