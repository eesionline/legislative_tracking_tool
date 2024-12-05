import webbrowser

def display_html_in_browser(summary_html, file_name="bill_display.html"):
    # Create an HTML file and write the content
    with open(file_name, "w") as file:
        file.write(summary_html)

    # Open the file in the default web browser
    webbrowser.open(file_name)

# Example usage
summary_html = """
<p><b>Get Rewarding Outdoor Work for our Veterans Act or the GROW Act</b></p>
<p>This bill addresses certain federal activities related to veterans...</p>
"""
# display_html_in_browser(summary_html)
