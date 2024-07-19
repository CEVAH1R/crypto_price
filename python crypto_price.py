import requests
import time
from rich.console import Console
from rich.text import Text

# Yapımcı Bilgileri
CEVAH1R = "Your Name"  # Buraya adınızı yazın
GITHUB_PROFILE = "https://github.com/CEVAH1R"  # Buraya GitHub profil bağlantınızı yazın

def fetch_coin_data(coin_id):
    url = f'https://api.coingecko.com/api/v3/coins/{coin_id}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f'API isteği sırasında bir hata oluştu: {e}')
        return None

def display_coin_data(data):
    console = Console()

    # Yapımcı adı ve GitHub profili
    title = Text(f"MADE WİTH  BY CEVAH1R ", style="bold green")
    console.print(title, justify="center")
    
    profile_info = Text(f"  GitHub : {GITHUB_PROFILE}", style="bold cyan")
    console.print(profile_info, justify="center")
    
    console.print("\n" + "="*50 + "\n")
    
    if data:
        console.print("[bold cyan]Coin Information[/bold cyan]", style="bold underline")
        console.print(f"[bold]Coin Name:[/bold] {data.get('name', 'N/A')}")
        console.print(f"[bold]Symbol:[/bold] {data.get('symbol', 'N/A')}")
        console.print(f"[bold]Current Price (USD):[/bold] ${data['market_data']['current_price'].get('usd', 'N/A')}")
        console.print(f"[bold]Market Cap (USD):[/bold] ${data['market_data']['market_cap'].get('usd', 'N/A')}")
        console.print(f"[bold]24h Volume (USD):[/bold] ${data['market_data']['total_volume'].get('usd', 'N/A')}")
        console.print(f"[bold]High 24h (USD):[/bold] ${data['market_data']['high_24h'].get('usd', 'N/A')}")
        console.print(f"[bold]Low 24h (USD):[/bold] ${data['market_data']['low_24h'].get('usd', 'N/A')}")
        console.print(f"[bold]Circulating Supply:[/bold] {data['market_data'].get('circulating_supply', 'N/A')}")
        console.print(f"[bold]Total Supply:[/bold] {data['market_data'].get('total_supply', 'N/A')}")
        console.print(f"[bold]Max Supply:[/bold] {data['market_data'].get('max_supply', 'N/A')}")
    else:
        console.print("[bold red]No data available.[/bold red]")

def main():
    try:
        coin_id = input('Enter the Coin ID (e.g., bitcoin, ethereum): ').strip().lower()
        if coin_id:
            while True:
                data = fetch_coin_data(coin_id)
                display_coin_data(data)
                time.sleep(30)  # Belirli bir süre bekle
        else:
            print('Geçerli bir Coin ID girin.')
    except Exception as e:
        print(f'Beklenmedik bir hata oluştu: {e}')
    finally:
        # Terminal penceresinin kapanmasını engellemek için
        print("\nPress Enter to exit...")
        input()

if __name__ == "__main__":
    main()
