// Initialize AOS
AOS.init({
    duration: 1000,
    once: true
  });
  
  // Sector Distribution Chart
  new Chart(document.getElementById('sectorChart'), {
      type: 'pie',
      data: {
          labels: ['Consulting', 'Data Science', 'Research', 'BFSI'],
          datasets: [{
              data: [41.7, 23, 16.7, 16.7],
              backgroundColor: [
                  'rgba(59, 130, 246, 0.8)',
                  'rgba(251, 191, 36, 0.8)',
                  'rgba(16, 185, 129, 0.8)',
                  'rgba(239, 68, 68, 0.8)'
              ]
          }]
      },
      options: {
          responsive: true,
          plugins: {
              legend: {
                  position: 'bottom'
              }
          }
      }
  });
  
  // CTC Charts Configuration
  const ctcChartConfig = (data, label, color) => ({
      type: 'bar',
      data: {
          labels: ['2019-21', '2020-22', '2021-23', '2022-24'],
          datasets: [{
              label: label,
              data: data,
              backgroundColor: color,
              borderColor: color.replace('0.8', '1'),
              borderWidth: 1
          }]
      },
      options: {
          responsive: true,
          scales: {
              y: {
                  beginAtZero: true,
                  ticks: {
                      callback: function(value) {
                          return value + ' LPA';
                      }
                  }
              }
          },
          plugins: {
              legend: {
                  display: true,
                  position: 'top'
              },
              tooltip: {
                  callbacks: {
                      label: function(context) {
                          return context.dataset.label + ': ' + context.raw + ' LPA';
                      }
                  }
              }
          }
      }
  });
  
  // Mean CTC Chart
  new Chart(document.getElementById('meanCTCChart'), 
      ctcChartConfig([12, 12.5, 13, 13.6], 'Mean CTC (LPA)', 'rgba(59, 130, 246, 0.8)'));
  
  // Median CTC Chart
  new Chart(document.getElementById('medianCTCChart'),
      ctcChartConfig([11, 11.5, 12, 13], 'Median CTC (LPA)', 'rgba(251, 191, 36, 0.8)'));
  
  // Highest CTC Chart
  new Chart(document.getElementById('highestCTCChart'),
      ctcChartConfig([23, 24, 24, 25], 'Highest CTC (LPA)', 'rgba(16, 185, 129, 0.8)'));
  
  // Placement Statistics Chart
  const ctx = document.getElementById('placementChart').getContext('2d');
  const placementChart = new Chart(ctx, {
      type: 'bar',
      data: {
          labels: ['2018', '2019', '2020', '2021', '2022'],
          datasets: [{
              label: 'Placement Rate',
              data: [95, 97, 98, 99, 100],
              backgroundColor: 'rgba(54, 162, 235, 0.2)',
              borderColor: 'rgba(54, 162, 235, 1)',
              borderWidth: 1
          }]
      },
      options: {
          responsive: true,
          scales: {
              y: {
                  beginAtZero: true
              }
          },
          plugins: {
              legend: {
                  display: true,
                  position: 'top'
              },
              tooltip: {
                  callbacks: {
                      label: function(context) {
                          return context.dataset.label + ': ' + context.raw + '%';
                      }
                  }
              }
          }
      }
  });