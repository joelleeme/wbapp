const yearRangeForm = document.querySelector('#yearRangeForm');

if ('addEventListener' in yearRangeForm) {
    yearRangeForm.addEventListener('submit', handleSubmit);
} else {
    yearRangeForm.onsubmit = handleSubmit;
}

function handleSubmit(event) {
    event.preventDefault();

    const startYear = parseInt(document.getElementById('startYear').value);
    const endYear = parseInt(document.getElementById('endYear').value);

        fetch(`/api/real-estate/analysis?startYear=${startYear}&endYear=${endYear}`)
            .then(response => response.json())
            .then(data => {
                updateChart(data);
            })
            .catch(error => console.error('Error fetching real estate analysis data:', error));

    const testData = [];

    for (let i = startYear; i <= endYear; ++i) {
      testData.push({ year: i, saleamount: Math.floor(Math.random() * 100000 + 200000) });
    }

    drawTestChart(testData);
}

function drawTestChart(data) {
    const ctx = document.getElementById('realEstateChart').getContext('2d');
    const labels = data.map(entry => entry.year);
    const prices = data.map(entry => entry.saleamount);

    if (window.myLineChart) {
      window.myLineChart.destroy();
    }

    window.myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: labels,
          datasets: [{
              label: 'Random Sales Prices',
              backgroundColor: 'rgba(255, 99, 132, 0.2)',
              borderColor: 'rgb(255, 99, 132)',
              borderWidth: 1,
              fill: false,
              data: prices
          }]
        },
        options: {
          responsive: true,
          scales: {
            x: {
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Years'
                }
            },
            y: {
                display: true,
                beginAtZero: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Sales Amount ($)'
                }
            }
          }
        }
    });
}