from os import write
import streamlit as st
import pandas as pd
from lazypredict.Supervised import LazyRegressor
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import load_diabetes, load_boston
import matplotlib.pyplot as plt
import seaborn as sns
import base64
import io
# import random
#---------------------------------#
# Page layout
# Page expands to full width

st.set_page_config(page_title='AUTOMATED ML Model WEB APP',
                   layout='wide')
#---------------------------------#
# Model building


def build_model(df):
    df = df.loc[:100]  # FOR TESTING PURPOSE, COMMENT THIS OUT FOR PRODUCTION
    X = df.iloc[:, :-1]  # Using all column except for the last column as X
    Y = df.iloc[:, -1]  # Selecting the last column as Y

    st.markdown('**1.2. Dataset dimension**')
    st.write('X')
    st.info(X.shape)
    st.write('Y')
    st.info(Y.shape)

    st.markdown('**1.3. Variable details**:')
    st.write('X variable (first 20 are shown)')
    st.info(list(X.columns[:20]))
    st.write('Y variable')
    st.info(Y.name)

    # Build auto model
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=split_size, random_state=seed_number)
    reg = LazyRegressor(verbose=0, ignore_warnings=False, custom_metric=None)
    models_train, predictions_train = reg.fit(
        X_train, X_train, Y_train, Y_train)
    models_test, predictions_test = reg.fit(X_train, X_test, Y_train, Y_test)

    st.subheader('2. Table of Model Performance')

    st.write('Training set')
    st.write(predictions_train)
    st.markdown(filedownload(predictions_train, 'training.csv'),
                unsafe_allow_html=True)

    st.write('Test set')
    st.write(predictions_test)
    st.markdown(filedownload(predictions_test, 'test.csv'),
                unsafe_allow_html=True)

    st.subheader('3. Plot of Model Performance (Train set)')

    with st.markdown('**R-squared**'):
        # Tall
        predictions_test["R-Squared"] = [0 if i <
                                         0 else i for i in predictions_test["R-Squared"]]
        plt.figure(figsize=(3, 9))
        sns.set_theme(style="whitegrid")
        ax1 = sns.barplot(y=predictions_train.index,
                          x="R-Squared", data=predictions_train)
        ax1.set(xlim=(0, 1))
    st.markdown(imagedownload(plt, 'plot-r2-tall.pdf'), unsafe_allow_html=True)
    # Wide
    plt.figure(figsize=(9, 3))
    sns.set_theme(style="whitegrid")
    ax1 = sns.barplot(x=predictions_train.index,
                      y="R-Squared", data=predictions_train)
    ax1.set(ylim=(0, 1))
    plt.xticks(rotation=90)
    st.pyplot(plt)
    st.markdown(imagedownload(plt, 'plot-r2-wide.pdf'), unsafe_allow_html=True)

    with st.markdown('**RMSE (capped at 50)**'):
        # Tall
        predictions_test["RMSE"] = [
            50 if i > 50 else i for i in predictions_test["RMSE"]]
        plt.figure(figsize=(3, 9))
        sns.set_theme(style="whitegrid")
        ax2 = sns.barplot(y=predictions_train.index,
                          x="RMSE", data=predictions_train)
    st.markdown(imagedownload(plt, 'plot-rmse-tall.pdf'),
                unsafe_allow_html=True)
    # Wide
    plt.figure(figsize=(9, 3))
    sns.set_theme(style="whitegrid")
    ax2 = sns.barplot(x=predictions_train.index,
                      y="RMSE", data=predictions_train)
    plt.xticks(rotation=90)
    st.pyplot(plt)
    st.markdown(imagedownload(plt, 'plot-rmse-wide.pdf'),
                unsafe_allow_html=True)

    with st.markdown('**Calculation time**'):
        # Tall
        predictions_test["Time Taken"] = [
            0 if i < 0 else i for i in predictions_test["Time Taken"]]
        plt.figure(figsize=(3, 9))
        sns.set_theme(style="whitegrid")
        ax3 = sns.barplot(y=predictions_train.index,
                          x="Time Taken", data=predictions_train)
    st.markdown(imagedownload(plt, 'plot-calculation-time-tall.pdf'),
                unsafe_allow_html=True)
    # Wide
    plt.figure(figsize=(9, 3))
    sns.set_theme(style="whitegrid")
    ax3 = sns.barplot(x=predictions_train.index,
                      y="Time Taken", data=predictions_train)
    plt.xticks(rotation=90)
    st.pyplot(plt)
    st.markdown(imagedownload(plt, 'plot-calculation-time-wide.pdf'),
                unsafe_allow_html=True)


# Download CSV data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df, filename):
    csv = df.to_csv(index=False)
    # strings <-> bytes conversions
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download={filename}>Download {filename} File</a>'
    return href


def imagedownload(plt, filename):
    s = io.BytesIO()
    plt.savefig(s, format='pdf', bbox_inches='tight')
    plt.close()
    # strings <-> bytes conversions
    b64 = base64.b64encode(s.getvalue()).decode()
    href = f'<a href="data:image/png;base64,{b64}" download={filename}>Download {filename} File</a>'
    return href


#---------------------------------#
st.write("""
# AUTOMATED ML Model WEB APP

This is implemented by using Python and **lazypredict** library building several machine learning models at once.

✨ **Developed by: | Vedula N.B.S Mahathi - 18671A1951 | Department of Electronics and Computer Engg | JBIET | **

___

""")

#---------------------------------#
# Sidebar - Collects user input features into dataframe
with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader(
        "Upload your input CSV file", type=["csv"])
    st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)
""")

# Sidebar - Specify parameter settings
with st.sidebar.header('2. Set Parameters'):
    split_size = st.sidebar.slider(
        'Data split ratio (% for Training Set)', 10, 90, 80, 5)
    seed_number = st.sidebar.slider(
        'Set the random seed number', 1, 100, 42, 1)


#---------------------------------#
# Main panel

# Displays the dataset
st.write("""
# 📌Dont have a data set? Want to know through business problem?
""")
sequence = st.selectbox("Select from here?", [
    "", 'Prediction', 'Identification', 'Deep Learning'])
algolist = ["1) Random Forest Regression\n 2) Logistic Regression\n 3) Linear Regression",
            "1) Logistic Regression, 2) Decision Tree, 3) Random Forest, 4) Navie Bayers", "1) CNN, 2) RNN, 3) gradient Descent"]
if sequence == 'Prediction':
    st.write("The Required Algorigthms would be:")
    st.write(algolist[0])
elif sequence == "Identification":
    st.write("The Required Algorigthms would be:")
    st.write(algolist[1])
elif sequence == "Deep Learning":
    st.write("The Required Algorigthms would be:")
    st.write(algolist[2])
else:
    st.write("know your algorithm!")

st.write("""
# 📌Select this if u have a data set!
# or click the button below to upload the existing example data set
""")

st.subheader('1. Dataset')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.markdown('**1.1. Glimpse of dataset**')
    st.write(df)
    build_model(df)
else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to use Example Dataset'):
        # Diabetes dataset
        # diabetes = load_diabetes()
        # X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
        # Y = pd.Series(diabetes.target, name='response')
        # df = pd.concat( [X,Y], axis=1 )

        # st.markdown('The Diabetes dataset is used as the example.')
        # st.write(df.head(5))

        # Boston housing dataset
        boston = load_boston()
        # X = pd.DataFrame(boston.data, columns=boston.feature_names)
        # Y = pd.Series(boston.target, name='response')
        # FOR TESTING PURPOSE, COMMENT THIS OUT FOR PRODUCTION
        X = pd.DataFrame(boston.data, columns=boston.feature_names).loc[:100]
        # FOR TESTING PURPOSE, COMMENT THIS OUT FOR PRODUCTION
        Y = pd.Series(boston.target, name='response').loc[:100]
        df = pd.concat([X, Y], axis=1)

        st.markdown('The Boston housing dataset is used as the example.')
        st.write(df.head(5))

        build_model(df)
