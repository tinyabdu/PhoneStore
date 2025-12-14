import flet as ft



stats = [
    ("Total revenue", "$99,560", "+2.5%", "#14532D"),
    ("Total orders", "35", "-1.2%", "#7F1D1D"),
    ("Total visitors", "45,600", "+5.1%", "#1E3A8A"),
    ("Net profit", "$60,450", "+3.7%", "#064E3B"),
]


def revenue_chart():
    return ft.BarChart(
        expand=True,
        bar_groups=[
            ft.BarChartGroup(
                x=i,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=value,
                        width=18,
                        border_radius=6,
                    )
                ],
            )
            for i, value in enumerate([12000, 8000, 10000, 9000, 11000, 14000, 16000])
        ],
        left_axis=ft.ChartAxis(
            labels_size=40,
            title=ft.Text("Revenue"),
        ),
        bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(value=i, label=ft.Text(m))
                for i, m in enumerate(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"])
            ],
            labels_size=30,
        ),
        tooltip_bgcolor="#1F2937",
        max_y=18000,
    )




def stat_card(title: str, value: str, percent: str, color: str):
    return ft.Container(
        height=140,
        bgcolor="#121212",
        border_radius=18,
        padding=15,
        col={"xs": 12, "sm": 6, "md": 3},
        content=ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Text(title, color="#C2C2CE", size=14),
                ft.Text(value, size=26, weight=ft.FontWeight.BOLD, color="#A1A1A5"),
                ft.Container(
                    padding=ft.padding.symmetric(horizontal=8, vertical=4),
                    bgcolor=color,
                    border_radius=20,
                    content=ft.Text(percent, size=12, color="#B0B0B6"),
                ),
            ],
        ),
    )


def Home(page: ft.Page):
    
    
    
    # # Sample chart data for analysis
    # chart = ft.LineChart(
    #     width=600,
    #     height=300,
    #     min_y=0,
    #     data_series=[
    #         ft.LineChartData(
    #             data_points=[
    #                 ft.LineChartDataPoint(1, 150),
    #                 ft.LineChartDataPoint(2, 200),
    #                 ft.LineChartDataPoint(3, 250),
    #                 ft.LineChartDataPoint(4, 300),
    #                 ft.LineChartDataPoint(5, 400),
    #                 ft.LineChartDataPoint(6, 350),
    #                 ft.LineChartDataPoint(7, 500),
    #             ]
    #         )
    #     ]
    # )


    return ft.Container(
        expand=True,
        padding=20,
        content=ft.Column(
            expand=True,
            spacing=25,
            controls=[
                # HEADER
                ft.Column(
                    spacing=4,
                    controls=[
                        ft.Text("Hello, Tinyabdu",
                                size=32,
                                weight=ft.FontWeight.BOLD,
                                color="#0A0A0A"
                        ),
                        ft.Text(
                            "This is what’s happening in your store this month",
                            color="#131212",
                        ),
                    ],
                ),

                # STATS 
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        stat_card("Total Income", "$99,560", "+2.5%", "#14532D"),
                        stat_card("Total Buyers", "35", "-1.2%", "#7F1D1D"),
                        stat_card("Total Items", "45,600", "+5.1%", "#1E3A8A"),
                        stat_card("Net profit", "$60,450", "+3.7%", "#064E3B"),
                    ],
                ),
                

                #ANALYSIS SECTION 
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        # MAIN CHART
                        ft.Container(
                            height=380,
                            col={"xs": 12, "md": 8},
                            bgcolor="#121212",
                            border_radius=18,
                            padding=20,
                            content=ft.Column(
                                expand=True,
                                spacing=10,
                                controls=[
                                    ft.Text(
                                        "Revenue Analysis",
                                        size=18,
                                        weight=ft.FontWeight.BOLD,
                                        color="#C2C2CE",
                                    ),
                                    ft.Text(
                                        "This month vs last month",
                                        size=12,
                                        color="#9CA3AF",
                                    ),

                                    # CHART PLACEHOLDER
                                    ft.Container(
                                        expand=True,
                                        alignment=ft.alignment.center,
                                        border_radius=12,
                                        bgcolor="#1F1F23",
                                        content=revenue_chart()
                                    ),
                                ],
                            ),
                        ),

                        # SIDE ANALYSIS 
                        ft.Column(
                            col={"xs": 12, "md": 4},
                            spacing=20,
                            controls=[
                                ft.Container(
                                    height=180,
                                    bgcolor="#121212",
                                    border_radius=18,
                                    padding=20,
                                    content=ft.Column(
                                        spacing=10,
                                        controls=[
                                            ft.Text(
                                                "Buyers",
                                                size=16,
                                                weight=ft.FontWeight.BOLD,
                                                color="#E4E7EE",
                                            ),
                                            ft.Text(
                                                "98 Sold",
                                                color="#89898D",
                                                size=28,
                                                weight=ft.FontWeight.BOLD,
                                            ),
                                            ft.Text(
                                                "12 orders awaiting confirmation",
                                                color="#9CA3AF",
                                            ),
                                        ],
                                    ),
                                ),
                                ft.Container(
                                    height=180,
                                    bgcolor="#121212",
                                    border_radius=18,
                                    padding=20,
                                    content=ft.Column(
                                        spacing=10,
                                        controls=[
                                            ft.Text(
                                                "Customers",
                                                size=16,
                                                weight=ft.FontWeight.BOLD,
                                                color="#E4E7EE",
                                            ),
                                            ft.Text(
                                                "17 customers",
                                                color="#89898D",
                                                size=28,
                                                weight=ft.FontWeight.BOLD,
                                            ),
                                            ft.Text(
                                                "Waiting for response",
                                                color="#9CA3AF",
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
    )

