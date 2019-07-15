#1. setup environemnt, import data
import pandas as pd
df = pd.read_excel("Unemployment.xls", sheet_name = "Unemployment Med HH Inc", skiprows = 7)

#2. investigate data, rename columns if necessary
print(df.info())
df.rename(columns = {"FIPS" : "County_code"}, inplace=True)

#it seems there are NaN values due to missing data in some years
#if the data is changed from wide to long data (reshape) NaN values will be removed

#3. divide df into 4 tables, create modular dataframes and focus on the data to be restructured:
#county_info, county_category, county_emp, county_hh
#county_info: state, code
#county_category: county category data based on urban and rural codes of 2013
#county_emp: employment data per county -data to be restructured-
#county_hh: county household prediction and data of 2017
county_info = df[["County_code", "State",  "Area_name" ]]
county_category = df[["County_code", "Rural_urban_continuum_code_2013", "Urban_influence_code_2013", "Metro_2013"]]
county_emp = df[["County_code", "Civilian_labor_force_2007", "Employed_2007", "Unemployed_2007", "Unemployment_rate_2007", "Civilian_labor_force_2008", "Employed_2008", "Unemployed_2008", "Unemployment_rate_2008", "Civilian_labor_force_2009", "Employed_2009", "Unemployed_2009", "Unemployment_rate_2009", "Civilian_labor_force_2010", "Employed_2010", "Unemployed_2010", "Unemployment_rate_2010", "Civilian_labor_force_2011", "Employed_2011", "Unemployed_2011", "Unemployment_rate_2011", "Civilian_labor_force_2012", "Employed_2012", "Unemployed_2012", "Unemployment_rate_2012", "Civilian_labor_force_2013", "Employed_2013", "Unemployed_2013", "Unemployment_rate_2013", "Civilian_labor_force_2014", "Employed_2014", "Unemployed_2014", "Unemployment_rate_2014", "Civilian_labor_force_2015", "Employed_2015", "Unemployed_2015", "Unemployment_rate_2015", "Civilian_labor_force_2016", "Employed_2016", "Unemployed_2016", "Unemployment_rate_2016", "Civilian_labor_force_2017", "Employed_2017", "Unemployed_2017", "Unemployment_rate_2017"]]
county_hh = df[["County_code", "Median_Household_Income_2017", "Med_HH_Income_Percent_of_State_Total_2017"]]

#4. restructure county employement data from wide data to long to eliminate NA values
#change county code column to index to make reshaping easier
county_emp = county_emp.set_index("County_code", drop=True, inplace=False)

#rename column headers with Multiindex columns so that year will be in level 0, employement data will be level 1
county_emp.columns = pd.MultiIndex.from_product([["2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017"], ["Civilian_labor_force", "Employed", "Unemployed", "Unemployment_rate"]])

#pass year column as index to stack the employement data 
county_emp = county_emp.stack(level=0)

#5. clean up data using lambda, and ordering of indexes and columns
#add year and county code back as column
county_emp["Tuple"] = county_emp.index
county_emp["County_code"] = county_emp.Tuple.apply(lambda x: x[0])
county_emp["Year"] = county_emp.Tuple.apply(lambda x: x[1])

#rearrange county_emp column orders and indexes
county_emp = county_emp.reset_index(drop=True, inplace=False)
county_emp = county_emp[["County_code", "Year", "Civilian_labor_force", "Employed", "Unemployed", "Unemployment_rate"]]
print(county_emp.info())

#6. increase the accuracy of the dataframe
county_emp["Unemployement_rate"] = county_emp["Unemployed"] / county_emp["Civilian_labor_force"]

#end of data cleaning
#7. write 4 dataframes in one excel and different sheets
dflist = [county_info, county_category, county_emp, county_hh]
sheetlist = ['county_info', 'county_category', 'county_emp', 'county_hh']
i=0
with pd.ExcelWriter('/home/cereyniyim/PythonProjects/Data_Cleaning_Project/test.xls') as writer:
    while i<len(dflist):
        dflist[i].to_excel(writer,sheet_name=sheetlist[i])
        i += 1
