var dataPoints1 = [],
    dataPoints2 = [];
var stockChart;
window.onload = function () {
    stockChart = new CanvasJS.StockChart("chartContainer", {
        // animationEnabled: true,
        exportEnabled: true,
        exportFileName: "StockChart", //Change it to "Stock Chart"
        theme: "light2",
        title: {
            text: "股票走勢圖",
            fontSize: 28,
            fontWeight: "bold",
        },

        // rangeChanged: rangeChanged,
        rangeSelector: {
            enabled: false, //change it to true
        },
        charts: [{
            axisX: {
                valueFormatString: "YYYY-MM-DD",
                crosshair: {
                    enabled: true,
                    snapToDataPoint: true
                }
            },
            axisY: {
                title: "Price(NT$)",
                prefix: "$"
            },
            toolTip: {
                shared: true
            },
            data: [{
                name: "Price (NT$)",
                type: "candlestick",
                xValueFormatString: "YYYY MMM DD",
                yValueFormatString: "$#,###.##",
                // axisYType: "secondary",
                risingColor: "green",
                fallingColor: "red",
                dataPoints: dataPoints1
            }]
        }],
        navigator: {
            // dynamicUpdate: false,
            data: [{
                dataPoints: dataPoints2
            }],
            // slider: {
            //     minimum: new Date(now_year, now_month-3, now_date),
            //     maximum: new Date(now_year, now_month+1, now_date)
            // }
        }
    });

    // function addData(data) {
    //     stockChart.options.charts[0].data[0].dataPoints = [];
    //     for (var i = 0; i < data.length; i++) {
    //         stockChart.options.charts[0].data[0].dataPoints.push({
    //             x: new Date(data[i].dateTime * 1000),
    //             y: [Number(data[i].open), Number(data[i].high), Number(data[i].low), Number(data[i].close)]
    //         });
    //     }
    //     stockChart.render();
    // }

    // function rangeChanged(e) {
    //     var minimum = parseInt(e.minimum / 1000);
    //     var maximum = parseInt(e.maximum / 1000);
    //     var url = "https://canvasjs.com/services/data/datapoints-bitcoinusd.php?minimum=" + minimum + "&maximum=" +
    //         maximum;
    //     $("#loader").css("display", "block");
    //     $.getJSON(url, function (data) {
    //         addData(data);
    //         $("#loader").css("display", "none");
    //     });
    // }
    stockChart.render();
    $("#loader").css("display", "block");
    // var now = new Date();
    // var now_year = now.getFullYear(); //得到年份
    // var now_month = now.getMonth(); //得到月份
    // var now_date = now.getDate(); //得到日期
    // var Today = new Date();
    // console.log("今天日期是 " + Today.getFullYear() + " 年 " + (Today.getMonth() + 1) + " 月 " + Today.getDate() + " 日");
    // console.log(now_year, now_month, now_date);
    // console.log(Date().now());
    // $.getJSON("https://canvasjs.com/services/data/datapoints-bitcoinusd.php", function (data) {
    //     for (var i = 0; i < data.length; i++) {
    //         dataPoints1.push({
    //             x: new Date(data[i].dateTime * 1000),

    //             y: [Number(data[i].open), Number(data[i].high), Number(data[i].low), Number(data[i].close)]
    //         });
    //         // console.log(new Date(data[i].dateTime * 1000));
    //         dataPoints2.push({
    //             x: new Date(data[i].dateTime * 1000),
    //             y: Number(data[i].close)
    //         });
    //     }
    //     console.log(dataPoints1);
    //     // console.log("{{ open|escapejs}}");
    //     // console.log(pp);
    //     $("#loader").css("display", "none");
    //     stockChart.render();

    // });


}
// var pp;
// function jsFunc(p){
//     console.log(p);
//     pp =  p;
// }

// console.log({{ open|escapejs}});