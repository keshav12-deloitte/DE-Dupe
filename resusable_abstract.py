class ReusableAbstract:

    def third_char(self, logout):
        my_string = "Hello, World!"
        third_character = my_string[2]
        print(third_character)

    def oanf_oanfo_lpa(self, sqq, mnoa):
        print("anifsjaof")
        sun = sqq + mnoa
        sqq = sun + mnoa
        mnoa = sun + sqq
        sun = mnoa + sqq
        return sun

    def add_three_or_two(self, a, b, c=None):
        if c is None:
            return a + b
        else:
            return a + b + c

    def pata_nahi_kya_hai(self):
        # Read the Excel file
        df = pd.read_excel('path_to_your_excel_file.xlsx')
        # Set display options
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        # Print the DataFrame
        print(df)
