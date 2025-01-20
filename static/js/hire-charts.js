document.addEventListener('DOMContentLoaded', function() {
    // Placement Statistics Chart
    const placementCtx = document.getElementById('placementChart').getContext('2d');
    new Chart(placementCtx, {
        type: 'bar',
        data: {
            labels: ['2020', '2021', '2022', '2023'],
            datasets: [{
                label: 'Placement Rate (%)',
                data: [85, 88, 92, 95],
                backgroundColor: 'rgba(0, 123, 255, 0.5)',
                borderColor: 'rgba(0, 123, 255, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100
                }
            }
        }
    });

    // Domain Distribution Chart
    const domainCtx = document.getElementById('domainChart').getContext('2d');
    new Chart(domainCtx, {
        type: 'pie',
        data: {
            labels: ['Analytics', 'Consulting', 'Research', 'General'],
            datasets: [{
                data: [30, 25, 20, 25],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.8)',
                    'rgba(54, 162, 235, 0.8)',
                    'rgba(255, 206, 86, 0.8)',
                    'rgba(75, 192, 192, 0.8)'
                ]
            }]
        },
        options: {
            responsive: true
        }
    });
});