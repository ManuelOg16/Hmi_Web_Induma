var on_green73_js
var number_piecesjs
var referencejs
var hrsreference
var oee
function get_troqueladora73(){ 

            if (on_green73_js==1){
                document.getElementById("led-red-73").setAttribute("stop-color","#000000"  )
                }
                else if (on_green73_js==0){ document.getElementById("led-red-73").setAttribute("stop-color","#ff0000")
                }
                if (on_green73_js==0){
                document.getElementById("led-green-73").setAttribute("stop-color","#000000"  )
                }
                else if (on_green73_js==1){ document.getElementById("led-green-73").setAttribute("stop-color","#06d306")
                }
    $.getJSON("troqueladora73",
       function (data1) {
            number_piecesjs=(data1.number_pieces)
            referencejs=(data1.reference);
            on_green73_js=(data1.on);
            // Build the chart
            hrsreference=referencejs*6;
            oee= (number_piecesjs*100)/hrsreference;
            // Make monochrome colors
            var pieColors = (function () {
                var colors = [],
                    base = Highcharts.getOptions().colors[0],
                    i;

                for (i = 0; i < 10; i += 1) {
                    // Start out with a darkened base color (negative brighten), and end
                    // up with a much brighter color
                    colors.push(Highcharts.color(base).brighten((i - 3) / 7).get());
                }
                return colors;
            }());
            Highcharts.chart('pie-chart-t73', {
                chart: {
                    plotBackgroundColor: null,
                    plotBorderWidth: null,
                    plotShadow: false,
                    type: 'pie',
                    backgroundColor: {
                        linearGradient: [0, 0, 500, 500],
                        stops: [  
                        [0, '#F7F6FB'],
                        [1, '#3e3e40']
                        ]}
                },
                title: {
                    text: ''
                },
                tooltip: {
                    pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
                },
                accessibility: {
                    point: {
                        valueSuffix: '%'
                    }
                },
                plotOptions: {
                    pie: {
                        allowPointSelect: true,
                        cursor: 'pointer',
                        colors: pieColors,
                        align: 'right',
                        dataLabels: {
                            enabled: true,
                            format: '<b>{point.name}</b><br>{point.percentage:.1f} %',
                            distance: -10,
                            style: {
                                fontSize: '0.9rem',
                                fontFamily: 'Roboto, sans-serif'
                            },
                            filter: {
                                property: 'percentage',
                                operator: '>',
                                value: 4
                            }
                        }
                    }
                },
                series: [{
                    name: 'Share',

                    data: [
                        { name: 'Oee', y: oee },
                        { name: '', y: 100-oee },

                    ],
                }]
            });
            Highcharts.chart('graph-troqueladora73', {
                chart: {
                    type: 'column',
                    backgroundColor: {
                        linearGradient: [0, 0, 500, 500],
                        stops: [  
                        [0, '#F7F6FB'],
                        [1, '#3e3e40']
                        ]}
                },
                title: {
                    text: '#73',
                    style: {
                        color: '#000',
                        font: 'bold 1.5rem "Roboto", Verdana, sans-serif'
                    }
                },
                subtitle: {
                    text: ''
                },
                xAxis: {
                    categories: [
                        'Piezas',
            
                    ],
                    labels: {
                        style: {
                            color: '#333',
                            fontWeight: 'bold',
                            fontSize: '1rem',
                            fontFamily: 'Roboto, Verdana, sans-serif'
                        }
                    },
                    crosshair: true
                },
                yAxis: {
                    min: 0,
                        //title: {
                        //text: '(Unidades)'}
                    title: {
                        style: {
                            color: '#A0A0A3'
                        }
                        },
                        title: {text: 'Unidades',
                            style: {
                                color: '#333',
                                fontWeight: 'bold',
                                fontSize: '1rem',
                                fontFamily: 'Roboto, Verdana, sans-serif'
                            }
                        }
                },
                plotOptions: {
                    column: {
                        pointPadding: 0.0,
                        borderWidth: 0
                    }
                },
                series: [{
                    name: 'Real',
                    data: [number_piecesjs],
                    dataLabels: {
                        enabled: true,
                        rotation: -90,
                        color: '#FFFFFF',
                        align: 'right',
                        format: '{point.y:.1f}', // one decimal
                        y: 2, // 10 pixels down from the top
                        style: {
                            fontSize: '0.8rem',
                            fontFamily: 'Roboto, sans-serif'
                        }
                    } 
            
                }, {
                    name: 'Esperado',
                    data: [referencejs]
                }],    
            }); 
        }
    );
}
setInterval('get_troqueladora73()', 4000); 