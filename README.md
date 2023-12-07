# MGT4250 Course Project Fall 2023
### Data Visualization & Storytelling - Elon University

### Jacquelyn Banford

[Link to Treemap - Visualization I](https://prod-useast-b.online.tableau.com/t/jbanford/views/VisualizationI/Sheet1?:origin=card_share_link&:embed=n)

[Link to Choropleth Map - Visualization II](https://prod-useast-b.online.tableau.com/t/jbanford/views/ChoroplethMapVisualizationII/Sheet1?:origin=card_share_link&:embed=n)

[Link to Pie Chart - Visualization III](https://github.com/jbanford/mgt4250test/blob/main/visual3.py)

### Questions of Interest 
1. What are the dominant music genres over the past 10 years, and how do they compare in terms of popularity and market share?
2. How does the popularity of music genres vary across different states in the America, and what regional patterns or trends emerge?
3. How have the proportions of the top 10 music genres changed over the past decade, and what insights can be drawn from these temporal trends?
### Data Description 
1. My treemap is accessible via the link on the top of this repository. It brings the viewers to the treemap formed on tableau. I complied a list of the top 10 songs from 2012-2022 and their respective genres then created an excel table of each genre and their frequencies. Using this data, I designed a treemap to visualize the most dominant genres in the top 10 songs over the past decade.
2. The choropleth map is also available through the link above and depicts the most popular genre by state in the United States. I created an excel sheet with columns "State" and "Genre" which, when put into tableau, formed a visual representation of the most popular genre by state. This allows a simple way to visualize regional preferences in music.
3. The final visualization can be accessed by clicking the link and running the python code to access the streamlit page. I focused on the columns "Year" and "Genre" with year being an integer and genre being a type object in the data. The genre column allows us to identify and analyze unique values and the platform uses year to filter by specific year from 2012-2022.
### Interpreting Visualizations
1. The treemap visualization illustrates the dominance of specific music genres over the past decade, highlighting their relative market share and popularity. The larger rectangles represent genres with a higher share, offering a visual snapshot of the industry's landscape. Understanding these dominant genres provides valuable insights into the evolving preferences of music consumers. This information is crucial for artists, producers, and record labels to make informed decisions about the type of music to create, invest in, and promote. It also helps streaming platforms tailor their recommendations which improves user engagement and satisfaction.
2. The choropleth map visually displays the geographical distribution of music genre preferences across states. Variances in color indicate the prevelance of the top genres listed. Understanding regional variations in music preferences is critical for tailoring marketing and promotional strategies to specific demographics. Artists and management labels can use this information to optimize concert tours, target promotional campaigns, and develop a resonance with local markets. Such a visualization exposes the cultural diversity within the music industry, fostering a deeper appreciation for different genres in various parts of the nations cultural landscape.
3. The pie chart, with its temporal filter, provides a dynamic view of how the popularity of different genres has evolved over the years. Changes in slice sizes reflect shifting trends which is essential for identifying emerging patterns, cultural shifts, and cyclical trends. This information is invaluable for stakeholders in the music industry to anticipate future market trends, make strategic decisions on artist signings and promotions, and adapt their business models to stay relevant in such a dynamic and ever-evolving market. 
## Discussion & Summary
[Link to article](https://royalsocietypublishing.org/doi/10.1098/rsos.171274)

This article provides an in-depth analysis of the dynamics influencing the success of songs in the music industry spanning over the last three decades, and leverages a vast dataset of over 500,000 songs. The findings expose interesting temporal trends, specifically a notable decrease in "happy" and "bright" songs, countered by a rise in "sad" songs, as well as a multi-decadal increase in dancing songs. This is in alignment with current preferences of pop and electronic over traditional genres such as classical and jazz, but it was still challenging to predict song success solely based on mood characteristics. The author tried to apply machine learning as a prediction method based on acoustic features and on historical trends of top songs but the study encountered challenges with a prediction accuracy of 0.74. By introducing what the study labeled as the "superstar variable", the machine predictions accuracy increased to 0.86. This aspect includes social popularity which serves as an influencial factor in song success on the charts. Overall, the study combined a detailed analysis of temporal trends, genre influences, and the characteristics of successful songs with machine learning approaches to predict success, revealing insights into the complex dynamics of the music industry.

## Chat GPT-4's Responses
1. "The dominant music genres over the past 10 years have been Pop, Hip-Hop/Rap, and EDM/Dance. Pop has been the most popular and has the largest market share, followed by Hip-Hop/Rap and EDM/Dance. Pop has been the most popular genre since the early 2000s, and its popularity has only grown over the past decade. Hip-Hop/Rap has also seen a surge in popularity over the past 10 years, and it is now the second most popular genre. EDM/Dance has also seen a rise in popularity, and it is now the third most popular genre."
2. "The popularity of music genres varies significantly across different states in the America. Generally, the most popular genres in the US are hip-hop, pop, rock, and country. However, there are regional patterns and trends that emerge when looking at the popularity of music genres across different states. For example, hip-hop is most popular in the South and West, while pop is most popular in the Midwest and Northeast. Rock is most popular in the Midwest and West, while country is most popular in the South and Midwest. Additionally, certain genres are more popular in certain states than others. For example, jazz is more popular in Louisiana, blues is more popular in Mississippi, and folk is more popular in the Appalachian region."
3. "Over the past decade, the proportions of the top 10 music genres have changed significantly. Pop music has seen a steady increase in popularity, while hip-hop and R&B have seen a steady decline. Rock music has seen a slight decline, while EDM and country music have seen a slight increase. Latin music has seen a significant increase in popularity, while jazz and classical music have seen a slight decline. The insights that can be drawn from these temporal trends are that music tastes are constantly changing and evolving. Pop music has become increasingly popular, while hip-hop and R&B have become less popular. EDM and Latin music have seen a surge in popularity, while rock music has seen a slight decline."

## Visualizations Compared to the Article and Chat GPT-4
My visulizations are in alignment with the premise of which the article is based and Chat GPT-4's responses to my questions of interest. The article aims at predicting the success of songs based on historical trends, predictions that benefit from the data expressed in my visualizations. There is a strong correlation between song success and current public preferences so the data in my choropleth map and pie chart aid in predicting the most popular genre of music to write. Chat GPT-4's responses also reflected my findings with Pop, Hip-Hop, and Electronic as the dominating genres. 
