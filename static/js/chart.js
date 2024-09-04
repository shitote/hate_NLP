const ctx = document.getElementById('myChart');
const nonHateProb = parseFloat(ctx.getAttribute('data-nonhate'));
const hateProb = parseFloat(ctx.getAttribute('data-hate'));

// Data for the chart
const data = {
  labels: ['Non-hate', 'Hate'],
  datasets: [{
    label: 'Hate Speech Analysis',
    data: [nonHateProb, hateProb],
    backgroundColor: ['#050', '#a00'],
    hoverOffset: 4
  }]
};

// Create the chart
new Chart(ctx, {
  type: 'doughnut', // or 'pie', 'bar', etc.
  data: data,
  options: {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      tooltip: {
        callbacks: {
          label: function (context) {
            let label = context.label || '';
            if (label) {
              label += ': ';
            }
            if (context.raw !== null) {
              label += context.raw.toFixed(2); // Rounds the value to 2 decimal places
            }
            return label;
          }
        }
      }
    }
  }
});
