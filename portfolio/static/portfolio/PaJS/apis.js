function coinFlip() {
    const options = {
        method: 'GET',
        headers: {
            'X-RapidAPI-Key': '9ea2f2d1f9mshe369a6605b315d1p1759e4jsn91705e689ef2',
            'X-RapidAPI-Host': 'coin-flip1.p.rapidapi.com'
        }
    };

    fetch('https://coin-flip1.p.rapidapi.com/headstails', options)
        .then(response => response.json())
        .then(response => {
            const coin = data;
            document.getElementById('coin').innerHTML = String(coin.outcome);
        });
}
