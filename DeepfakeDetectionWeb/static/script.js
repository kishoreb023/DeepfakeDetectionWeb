document.addEventListener("DOMContentLoaded", function () {
    if (typeof prediction !== "undefined" && typeof confidence !== "undefined") {
        const ctx = document.getElementById('confidenceChart').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Confidence'],
                datasets: [{
                    label: prediction,
                    data: [confidence],
                    backgroundColor: prediction === "Real"
                        ? "rgba(75, 192, 192, 0.7)"
                        : "rgba(255, 99, 132, 0.7)",
                    borderColor: prediction === "Real"
                        ? "rgba(75, 192, 192, 1)"
                        : "rgb(192, 2, 44)",
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true,
                        max: 100
                    }
                }
            }
        });
    }
});
