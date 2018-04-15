library(plotly)
setwd('/Users/m/code/Python/Trello')

trello <- read.csv("trello")
logDays <- log(trello$days)
trello$urgency <- 1-logDays/max(logDays)

p <- plot_ly(trello, x = ~urgency, y = ~importance, type = 'scatter', mode = 'markers+text',
             marker = list(size = ~complexity*5, opacity = 0.5),
             text = ~name,
             textposition = 'bottom',
             hoverinfo = ~name )%>%
  
  layout(title = 'Priorites',
         xaxis = list(showgrid = TRUE),
         yaxis = list(tickvals=~trello$importance,ticktext=~trello$importance))
p
