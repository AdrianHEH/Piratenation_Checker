import requests

def check_allocation(wallet_address):

    url = f"https://www.piratenation.foundation/api/merkle/two/{wallet_address}"
    
    response = requests.get(url)
    
    if response.status_code == 200:  # If the request is successful
        data = response.json()
        if 'data' in data:  # If the response contains 'data'
            allocation = data['data']
            
            hex_amount = allocation['amount']
            decimal_amount = int(hex_amount, 16)
            final_amount = decimal_amount / (10**18)

            print(f"Index: {allocation['index']}")
            print(f"Amount (Decimal): {decimal_amount}")
            print(f"Proof: {allocation['proof']}")
            print(f"Congratulations! You can claim {int(final_amount)} $pirate")
        else:
            print("No data found for this address.")
    else:
        print(f"Error {response.status_code}: Unable to retrieve data.")

print("\n")
wallet_address = input("Enter the wallet address: ")
check_allocation(wallet_address)
