import numpy as np

# for data frame
import pandas as pd

# visualization
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.tools as tls
import plotly.offline as py
from plotly.offline import init_notebook_mode, iplot, plot
import plotly.graph_objs as go

def process(path):
	df=pd.read_csv(path)
	# first five row from dataframe
	print(df.head())
	# number of different features for each features
	print(df.nunique())

	# find which columns contain any NaN value in Pandas dataframe
	print(df.columns[df.isna().any()].tolist())
	df = df.drop('Timestamp', 1)
	df = df.drop('comments', 1)
	df = df.drop('Gender', 1)
	df = df.drop('state', 1)

	df[['Age']].plot(kind='hist',bins=[0,10,20,30,40,50, 60, 70, 80],rwidth=0.8)
	plt.title('Age Histogram')
	plt.savefig('results/Age.png') 
	plt.pause(5)
	plt.show(block=False)
	plt.close()


	# plot for 'self_employed'

	df['self_employed'].value_counts().plot.bar()
	plt.title('Self Employed')
	plt.savefig('results/self_employed.png') 
	plt.pause(5)
	plt.show(block=False)
	plt.close()


	# We need encoding 'self_employed'. 

	df['self_employed'] = df['self_employed'].map({
	        'No': 0,
	        'Yes': 1         
	})

	# plot for 'family_history'

	df['family_history'].value_counts().plot.bar()
	plt.title('Family History')
	plt.savefig('results/family_history.png') 
	plt.pause(5)
	plt.show(block=False)
	plt.close()


	# We need encoding 'family_history'. 
	
	df['family_history'] = df['family_history'].map({
	        'No': 0,
	        'Yes': 1         
	})

	# plot for 'treatment'

	df['treatment'].value_counts().plot.bar()
	plt.title('Treatment')
	plt.savefig('results/treatment.png') 
	plt.pause(5)
	plt.show(block=False)
	plt.close()

	# We need encoding 'treatment'. 

	df['treatment'] = df['treatment'].map({
	        'No': 0,
	        'Yes': 1         
	})

	
	# plot for 'work_interfere'

	df['work_interfere'].value_counts().plot.bar()
	plt.title('Work Interfere Count')
	plt.savefig('results/work_interfere.png') 
	plt.pause(5)
	plt.show(block=False)
	plt.close()


	# encodding 'work_interfere'
	
	def apply_work_interfere(s):
	    if s == 'Never':
	        return 0
	    elif s == 'Rarely':
	        return 1
	    elif s == 'Sometimes':
	        return 2
	    elif s == 'sometimes':
	        return 2
	    elif s == 'Often':
	        return 3

	df['work_interfere'] = df['work_interfere'].apply(apply_work_interfere)
	# plot for 'work_interfere'


	# plot for 'no_employees'
	
	df['no_employees'].value_counts().plot.bar()


	# encodding 'no_employees'
	
	def apply_no_employees(s):
	    if s == '1-5':
	        return 0
	    elif s == '6-25':
	        return 1
	    elif s == '26-100':
	        return 2
	    elif s == '100-500':
	        return 3
	    elif s == '500-1000':
	        return 4
	    elif s == 'More than 1000':
	        return 5

	df['no_employees'] = df['no_employees'].apply(apply_no_employees)

	# plot for 'no_employees'
	
	df['no_employees'].value_counts().plot.bar()
	plt.title('No of Employees')
	plt.savefig('results/no_employees.png') 
	plt.pause(5)
	plt.show(block=False)
	plt.close()


	# plot for 'remote_work'
	df['remote_work'].value_counts().plot.bar()
	plt.title('Remote Work')
	plt.savefig('results/remote_work.png') 
	plt.pause(5)
	plt.show(block=False)
	plt.close()


	df['remote_work'] = df['remote_work'].map({
	        'No': 0,
	        'Yes': 1         
	})
	

	# plot for 'tech_company'
	
	df['tech_company'].value_counts().plot.bar()
	plt.title('Tech Company')
	plt.savefig('results/tech_company.png') 
	plt.pause(5)
	plt.show(block=False)
	plt.close()
	

	# We need encoding 'tech_company'. 
	
	df['tech_company'] = df['tech_company'].map({
	        'No': 0,
	        'Yes': 1         
	})
	
	# plot for 'benefits'
	
	df['benefits'].value_counts().plot.bar()
	plt.title('Benefits')
	plt.savefig('results/benefits.png') 
	plt.pause(5)
	plt.show(block=False)
	plt.close()



	df['benefits'] = df['benefits'].map({
	        "No": 0,
	        "Yes": 1, 
	        "Don't know": 2
	})

	# plot for 'care_options'
	
	df['care_options'].value_counts().plot.bar()
	plt.title('Care Options')
	plt.savefig('results/care_options.png') 
	plt.pause(5)
	plt.show(block=False)
	plt.close()

	# We need encoding 'care_options'. 
	
	df['care_options'] = df['care_options'].map({
	        "No": 0,
	        "Yes": 1, 
	        "Not sure": 2
	})
	
	# plot for 'wellness_program'
	
	df['wellness_program'].value_counts().plot.bar()
	plt.title('Wellness Program')
	plt.savefig('results/wellness_program.png') 
	plt.pause(5)
	plt.show(block=False)
	plt.close()


	# We need encoding 'wellness_program'. 
	df['wellness_program'] = df['wellness_program'].map({
	        "No": 0,
	        "Yes": 1, 
	        "Don't know": 2
	})

	# plot for 'seek_help'
	
	df['seek_help'].value_counts().plot.bar()
	plt.title('Seek Help')
	plt.savefig('results/seek_help.png') 
	plt.pause(5)
	plt.show(block=False)
	plt.close()


	# We need encoding 'seek_help'. 
	
	df['seek_help'] = df['seek_help'].map({
	        "No": 0,
	        "Yes": 1, 
	        "Don't know": 2
	})
	
	# plot for 'anonymity'
	
	df['anonymity'].value_counts().plot.bar()
	plt.title('Anonymity')
	plt.savefig('results/anonymity.png') 
	plt.pause(5)
	plt.show(block=False)
	plt.close()
	

	# We need encoding 'anonymity'. 
	
	df['anonymity'] = df['anonymity'].map({
	        "No": 0,
	        "Yes": 1, 
	        "Don't know": 2
	})

	# plot for 'leave'
	
	df['leave'].value_counts().plot.bar()
	plt.title('Leave')
	plt.savefig('results/leave.png') 
	plt.pause(5)
	plt.show(block=False)
	plt.close()
	

	# We need encoding 'leave'. 
	df['leave'] = df['leave'].map({
	        "Very easy": 0,
	        "Somewhat easy": 1, 
	        "Somewhat difficult": 2,
	        "Very difficult": 3,
	        "Don't know": 4
	})

	# plot for 'mental_health_consequence'
	df['mental_health_consequence'].value_counts().plot.bar()
	plt.title('Mental Health Consequence')
	plt.savefig('results/mental_health_consequence.png') 
	plt.pause(5)
	plt.show(block=False)
	plt.close()


	# We need encoding 'mental_health_consequence'. 
	df['mental_health_consequence'] = df['mental_health_consequence'].map({
	        "No": 0,
	        "Maybe": 1, 
	        "Yes": 2,
	})

	# plot for 'phys_health_consequence'
	df['phys_health_consequence'].value_counts().plot.bar()
	plt.title('Phys Health Consequence')
	plt.savefig('results/phys_health_consequence.png') 
	plt.pause(5)
	plt.show(block=False)
	plt.close()


	# We need encoding 'mental_health_consequence'. 
	df['phys_health_consequence'] = df['phys_health_consequence'].map({
	        "No": 0,
	        "Maybe": 1, 
	        "Yes": 2,
	})

	# plot for 'coworkers'
	df['coworkers'].value_counts().plot.bar()
	plt.title('Coworkers')
	plt.savefig('results/coworkers.png') 
	plt.pause(5)
	plt.show(block=False)
	plt.close()


	# We need encoding 'coworkers'. 
	df['coworkers'] = df['coworkers'].map({
	        "No": 0,
	        "Some of them": 1, 
	        "Yes": 2,
	})

	# plot for 'supervisor'
	df['supervisor'].value_counts().plot.bar()
	plt.title('Supervisor')
	plt.savefig('results/supervisor.png') 
	plt.pause(5)
	plt.show(block=False)
	plt.close()


	# We need encoding 'supervisor'. 
	df['supervisor'] = df['supervisor'].map({
	        "No": 0,
	        "Some of them": 1, 
	        "Yes": 2,
	})

	# plot for 'mental_health_interview'
	df['mental_health_interview'].value_counts().plot.bar()
	plt.title('Mental Health Interview')
	plt.savefig('results/mental_health_interview.png') 
	plt.pause(5)
	plt.show(block=False)
	plt.close()

	# We need encoding 'mental_health_interview'. 
	df['mental_health_interview'] = df['mental_health_interview'].map({
	        "No": 0,
	        "Maybe": 1, 
	        "Yes": 2,
	})

	# plot for 'phys_health_interview'
	df['phys_health_interview'].value_counts().plot.bar()
	plt.title('Phys Health Interview')
	plt.savefig('results/phys_health_interview.png') 
	plt.pause(5)
	plt.show(block=False)
	plt.close()

	# We need encoding 'phys_health_interview'. 
	df['phys_health_interview'] = df['phys_health_interview'].map({
	        "No": 0,
	        "Maybe": 1, 
	        "Yes": 2,
	})
	# plot for 'obs_consequence'
	df['obs_consequence'].value_counts().plot.bar()
	plt.title('Obs Consequence')
	plt.savefig('results/obs_consequence.png') 
	plt.pause(5)
	plt.show(block=False)
	plt.close()

	# We need encoding 'obs_consequence'. 
	df['obs_consequence'] = df['obs_consequence'].map({
	        "No": 0,
	        "Yes": 1,
	})
	# plot for 'mental_vs_physical'
	df['mental_vs_physical'].value_counts().plot.bar()
	plt.title('Mental vs Physical')
	plt.savefig('results/mental_vs_physical.png') 
	plt.pause(5)
	plt.show(block=False)
	plt.close()

	# encodding 'mental_vs_physical'
	def apply_mental_vs_physical(s):
	    if s == 'No':
	        return 0
	    elif s == "Yes":
	        return 1
	    elif s == "Don't know":
	        return 2
	    else:
	        return 2
       
	df['mental_vs_physical'] = df['mental_vs_physical'].apply(apply_mental_vs_physical)
	df['Country'].unique()

	# Convert 'USA','usa','The USA' to 'United States'
	i = 0 
	for c in df['Country']:
	    if c == 'The USA':
	        df['Country'][i] = 'United States'
	    elif c == 'USA':
	        df['Country'][i] = 'United States'
	    elif c == 'usa':
	        df['Country'][i] = 'United States'
	    i = i + 1
    
	df['Country'].unique()
	df['obs_consequence'].unique()   

	total_country = df["Country"].value_counts()
	obs_consequence_no = df[df["obs_consequence"] == 0]["Country"].value_counts()
	obs_consequence_yes = df[df["obs_consequence"] == 1]["Country"].value_counts()

	#First plot
	trace0 = go.Bar(
	    x=obs_consequence_no.index,
	    y=obs_consequence_no.values,
	    name="obs consequence| NO"
	)

	#Second plot
	trace1 = go.Bar(
	    x=obs_consequence_yes.index,
	    y=obs_consequence_yes.values,
	    name="obs consequence | YES"
	)

	#Third plot
	trace2 = go.Bar(
	    x=total_country.index,
	    y=total_country.values,
	    name="All Country"
	)

	#Creating the grid
	fig = tls.make_subplots(rows=2, cols=2, specs=[[{}, {}], [{'colspan': 2}, None]],subplot_titles=('No','Yes', "General country"))

	#setting the figs
	fig.append_trace(trace0, 1, 1)
	fig.append_trace(trace1, 1, 2)
	fig.append_trace(trace2, 2, 1)

	fig['layout'].update(showlegend=True, title="Mental health in different country",bargap=0.05)
	iplot(fig)


	df_with_country = df.copy()
	df_with_country.info()

	# We use one-hot-codding
	df_with_country = pd.get_dummies(df_with_country, columns = ['Country'])
	df_with_country.fillna(-999, inplace = True)
	print(df_with_country.columns)

	df_with_country.columns[df_with_country.isna().any()].tolist()
	
	df_with_country.to_csv("Cleaneddataset.csv")

	y = df_with_country['obs_consequence']

#process("dataset.csv")