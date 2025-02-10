library(languageserver)
library(shiny)
library(markdown)
library(dplyr)
library(ggplot2)
library(lubridate)
library(markdown)

setwd("C:/Users/Ian89/OneDrive/Documents/GitHub/TennisInsights/DataAnalytics")


# Define UI
ui <- fluidPage(
    titlePanel("Winner's Number of Aces Over Time"),
    fluidRow(
        column(12,
            includeMarkdown("info.md")  # Include markdown file
        )
    ),
    fluidRow(
        column(12,
        plotOutput("acePlot", height = "600px")
        )
    )
)

# Define server logic
server <- function(input, output) {
    output$acePlot <- renderPlot({
        # Define the path to the CSV files
        path <- "ATPMatchData"

        # Read and combine CSV files
        files <- list.files(path, pattern = "atp_matches_20[1-9][0-9]\\.csv$", full.names = TRUE)
        data_list <- lapply(files, read.csv)
        combined_data <- bind_rows(data_list)

        # Extract relevant columns and convert date to proper format
        combined_data <- combined_data %>%
            select(tourney_date, winner_age) %>%
            mutate(tourney_date = ymd(tourney_date))

        # Aggregate data by date
        aggregated_data <- combined_data %>%
            group_by(tourney_date) %>%
            summarize(total_w_aces = mean(winner_age, na.rm = TRUE))

        # Plot the data
        ggplot(aggregated_data, aes(x = tourney_date, y = total_w_aces)) +
            geom_line(color = "skyblue", size = 2) +
            labs(title = "Year vs Average age of Winners",
                 x = "Date",
                 y = "Average age of Winners") +
            scale_x_date(date_breaks = "1 year", date_labels = "%Y") +
            theme_minimal()
    })
}

# Run the application
shinyApp(ui = ui, server = server)