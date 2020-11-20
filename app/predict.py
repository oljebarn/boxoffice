import numpy as np
import joblib

## Get the model trained in the notebook

model = joblib.load('models/box_office_pred.joblib')


def preprocess(data):

    feature_values = {
        'budget': 300000,
        'popularity': 10,
        'runtime': 110.0,
        'actOrAdv': 1,
        'lan_cat': 1,
        'spielberg': 0,
        'top8dir': 0,
        'top4actor': 0,
        'isCollection': 0
    }


    # Parse the form inputs and return the defaults updated with values entered.

    for key in [k for k in data.keys() if k in feature_values.keys()]:
        feature_values[key] = data[key]

    return feature_values


def predict(data):
    """
    If debug, print various useful info to the terminal.
    """
 
    # Store the data in an array in the correct order:

    column_order = ['budget', 'popularity', 'runtime', 'actOrAdv',
                    'lan_cat', 'spielberg', 'top8dir', 'top4actor', 'isCollection']

    data = np.array([data[feature] for feature in column_order], dtype=object)
    
    pred = model.predict(data.reshape(1,-1))

    return pred


def postprocess(prediction):
    """
    Apply postprocessing to the prediction. E.g. validate the output value, add
    additional information etc. 
    """

    pred = prediction

    # Validate. As an example, if the output is an int, check that it is positive.
    try: 
        int(pred[0]) > 0
    except:
        pass

    # Make strings
    pred = str(pred[0])

    # Return
    return_dict = {'pred': pred }

    return return_dict