---
title: "Series 1"
queries:
    - series_1.sql
---

# Series 1
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


<DataTable data={stats} title="Macro Statistics" groupBy=name>
    <Column id=name title=Country />
    <Column id=source title=Type/>
    <Column id=mean title=Mean fmt=pct2/>
    <Column id=std title=StdDev fmt=pct2/>
</DataTable>


We can see that the United States has had the highest equity premium over the whole period, which is not that surprising, considering the growth of the US economy over the last few years. A big part of that can be attributed to the growth of the tech sector, but also (in my opinion) the lack of growth in Japan and France. Japan is in its unique situation, where it has dealt with historically low interest rates and a shrinking population, which has led to a stagnation of the economy. Also, the culture where its frowned upon to raise prices as it can be seen as greedy, leads to no inflation and no push for further growth. France, on the other hand, has had a lot of political turmoil over the last few years, which has led to a stagnation of the economy.


## United States
<LineChart
    data={series_usa}
    x=Date
    y=value
    yFmt=pct2
    series=source>
</LineChart>

## Japan
<LineChart
    data={series_japan}
    x=Date
    y=value
    yFmt=pct2
    series=source
/>

## France
<LineChart
    data={series_france}
    x=Date
    y=value
    yFmt=pct2
    series=source
/>