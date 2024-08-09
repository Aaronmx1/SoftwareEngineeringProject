import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import zmq


def trigger_function(*args, **kwargs):
  # Read the tab-separated text file into a DataFrame
  df = pd.read_csv('generalLedger.txt', delimiter='\t', header=None)
  
  # Aggregate Data
  df.columns = ['trans_ID', 'date', 'description', 'amount', 'category']
  category_sums = df.groupby('category')['amount'].sum()
  
  
  # Creating SUMMARY PDF
  with PdfPages('spending_by_category.pdf') as pdf:
    # Plot a Bar Chart
    plt.figure(figsize=(10, 6))
    category_sums.plot(kind='bar')
    plt.xlabel('Category')
    plt.ylabel('Total Spending')
    plt.title('Spending by Category')
    pdf.savefig()  # Save the current figure into the PDF
    plt.close()  # Close the figure to avoid overlap
  print("PDF #1 has been created successfully.")
  
  ##CREATING LARGEST TO SMALLEST
  # Ensure 'amount' column is interpreted as numeric
  df['amount'] = pd.to_numeric(df['amount'])
  # Sort the DataFrame by 'amount' in descending order
  df_sorted = df.sort_values(by='amount', ascending=False)
  # Plot a bar chart
  with PdfPages('purchases_largest_to_smallest.pdf') as pdf:
    plt.figure(figsize=(10, 6))
    plt.bar(df_sorted['description'], df_sorted['amount'], color='skyblue')
    plt.xlabel('Description')
    plt.ylabel('Amount')
    plt.title('Purchases from Largest to Smallest')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()  # Adjust layout to prevent clipping of ylabel
  # Save to PDF
    pdf.savefig()  # Save the current figure into the PDF
    plt.close()  # Close the figure to avoid overlap
  print("PDF #2 has been created successfully.")



def server():
  context = zmq.Context()
  socket = context.socket(zmq.REP)
  socket.bind("tcp://*:5555")
  while True:
      # Wait for the next request from the client
      print("Server is listening on port 5555...")
    
      message = socket.recv_string()
      print(f"Received request: {message}")
      # Call the trigger function
      response_data = trigger_function(message)
      # Send response back to client
      socket.send_string("Summary Initiated")
      print(f"Sent response: Summary Initiated")


if __name__ == "__main__":
  server()