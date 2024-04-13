//init graph
const ctx = document.getElementById("myChart");
const config = {
    type: 'bar',
    data: {
        labels: ["Jsx", "Wei", "Janice", "Capp"],
        datasets:[{
            label: 'Height',
            data: [165, 190, 165, 50],
            borderwidth: 1,
        },
        {
            label: 'Weight',
            data: [65, 90, 65, 20],
            borderwidth: 1,
        }
    ]
    },
}

const myChart = new Chart(ctx, config);

