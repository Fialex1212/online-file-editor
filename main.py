import streamlit as st
import pandas as pd


class App:
    def __init__(self):
        self.file = None
        self.data = None
        self.table = None

    def get_data(self):
        #get, read and output data
        try:
            self.file = st.file_uploader(":file_folder: Upload a file", type=(['csv', 'txt', 'xlsx', "xls"]))
            file_name = self.file.name
            st.write(file_name)
            self.data = pd.read_csv(file_name, encoding="ISO-8859-1")
            self.table = st.data_editor(self.data)
        except:
            st.write("None")

    def update_data(self):
        #update data
        if st.button("Update data"):
            self.table.to_csv(self.file.name, index=False)

    def main(self):
        #Set up settings for site
        st.set_page_config(page_title="Superstore!!!", page_icon=":bar_chart:", layout="wide")
        st.title(" :bar_chart: Sample superStore EDA")
        st.markdown("<style> div.block-container{padding-top: 1rem;}</style>", unsafe_allow_html=True)
        self.get_data()
        self.update_data()

if __name__ == '__main__':
    app = App()
    app.main()