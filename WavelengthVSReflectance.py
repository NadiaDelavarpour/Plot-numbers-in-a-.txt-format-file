#!/usr/bin/env python
# coding: utf-8

# In[8]:


import os
import matplotlib.pyplot as plt

# Set the directory path
directory = 'OneDrive - North Dakota University System'
wavelength = []
reflectance = []
# Loop over all the files in the directory
for filename in os.listdir(directory):
    # Check if the file has .txt extension
    if filename.endswith('.txt'):
        # Open the file
        with open(os.path.join(directory, filename), 'r') as file:
            # Read the contents of the file
            lines = file.readlines()
            for line in lines[21:]:
                value = line.split('	 ')
                if len(value) >= 2:
                    # Append the first value to the wavelength list
                    wavelength.append(float(value[0]))
                    # Append the second value to the reflectance list
                    reflectance.append(float(value[1]))
                
#print(f"wavelength: {wavelength}, reflectance: {reflectance} ")

plt.plot(wavelength, reflectance)

# Add labels and title
plt.xlabel('Wavelength (micrometer)')
plt.ylabel('Relectance (%)')
plt.title(lines[0])
# Display the plot
plt.show()
plt.savefig('my_plot.png')





# In[ ]:




