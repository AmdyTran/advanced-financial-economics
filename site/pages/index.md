---
title: "Series 1"
queries:
    - series_1.sql
---

<DateInput
    title="Start After"
    name=date_range
    data={series_1}
    dates=Date
/>

```sql series_1_filtered
SELECT * FROM ${series_1}
WHERE Date >= '${inputs.date_range.value}'
```

```sql series_usa
SELECT * FROM ${series_1_filtered}
WHERE name = 'USA'
AND source != 'equity_premium'
```

```sql series_france
SELECT * FROM ${series_1_filtered} WHERE name = 'France'
AND source != 'equity_premium'
```

```sql series_japan
SELECT * FROM ${series_1_filtered} WHERE name = 'Japan'
AND source != 'equity_premium'
```

```sql stats
SELECT 
    name,
    source,
    MEAN(value) as mean,
    STDDEV(value) as std
FROM ${series_1_filtered}
GROUP BY name, source
```

## Analysis of Economic Indicators Across US, Japan, and France

<DataTable data={stats} title="Macro Statistics" groupBy=name>
    <Column id=name title=Country />
    <Column id=source title=Type/>
    <Column id=mean title=Mean fmt=pct2/>
    <Column id=std title=StdDev fmt=pct2/>
</DataTable>


The United States has demonstrated the strongest overall economic performance among the three countries, with the highest equity premium over the observed period. This supremacy can be attributed to several factors:
- Highest mean real GDP growth (2.42%)
- Strong performance of the tech sector
- Most favorable risk-return relationship, offering higher returns (8.78% stock returns) with lower volatility (18.03%)
- Robust equity premium of 7.75%, significantly outperforming both Japan and France

Japan presents a unique case study in economic challenges:
- Lowest mean GDP growth (0.64%) reflecting long-term stagnation
- Historically low interest rates (0.59% mean)
- Cultural resistance to price increases hampering inflation and growth
- Demographic challenges with a shrinking population
- Highest market volatility (22.99% for stock returns) despite lower returns
- Modest equity premium of 3.97%

France occupies a middle ground but faces its own challenges:
- Intermediate GDP growth (1.51%) but closer to Japan than the US
- Political turmoil in recent years affecting economic stability
- Maintains slightly higher real interest rates (1.33%) compared to peers
- Second-highest market volatility with a 21.01% standard deviation
- Equity premium of 5.35%, positioning it between the US and Japan

The data clearly illustrates the divergent paths these economies have taken, with the US maintaining strong growth and market performance, while Japan grapples with stagnation and France navigates various economic and political challenges. The US market's combination of higher returns and lower volatility makes it particularly attractive to investors, explaining its sustained premium over the other markets.

### United States
<LineChart
    data={series_usa}
    x=Date
    y=value
    yFmt=pct2
    series=source>
</LineChart>

### Japan
<LineChart
    data={series_japan}
    x=Date
    y=value
    yFmt=pct2
    series=source
/>

### France
<LineChart
    data={series_france}
    x=Date
    y=value
    yFmt=pct2
    series=source
/>

<Note>
    Data Sources & Methodology:
    * Market Indices: S&P 500 (SPX Index), CAC 40 (CAC Index), Nikkei 225 (NKY Index)
    * Government Bonds: US 10Y (USGG10YR), France 10Y (GTFRF10YR), Japan 10Y (GJGB10 Index)
    * Economic Data: CPI YOY for each country (JNCPIYOY, FRCPIYOY, CPI YOY), Real GDP Growth (EHGDUSY, EHGDFRY, EHGDJPY)

    Methodology:
    Real interest rates were calculated using the Fisher equation (r = i - π), with nominal rates shifted forward one year to match realized inflation rates. Stock returns were computed using year-end values of market indices. All data was resampled to year-end frequency to ensure consistency across different reporting periods. Real GDP growth rates were divided by 100 to convert from percentage points to decimal form.

    Note: Bond yields were converted from basis points to decimal form (divided by 100) before calculations. Equity premium was calculated as the difference between realized stock returns and real interest rates.
</Note>