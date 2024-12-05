from pretty_html_table import build_table
import pandas as pd

df = pd.read_excel('df.xlsx')
html_table_blue_light = build_table(df, 'blue_light')

# Save to html file
with open('pretty_table.html', 'w') as f:
    f.write(html_table_blue_light)

# Compare to the pandas .to_html method:
with open('pandas_table.html', 'w') as f:
    f.write(df.to_html())