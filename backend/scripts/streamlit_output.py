import streamlit as st
import sys
import io
from datetime import datetime
from backtest_script import run_backtest  # Assuming your original script is named backtest_script.py

def main():
    st.title("Stock Trading Strategy Backtester")

    # User inputs
    initial_cash = st.number_input("Enter initial cash", min_value=1.0, value=10000.0, step=1000.0)
    start_date = st.date_input("Select start date", value=datetime(2020, 1, 1))
    end_date = st.date_input("Select end date", value=datetime.now())

    if st.button("Run Backtest"):
        if start_date >= end_date:
            st.error("Start date must be before end date.")
        else:
            # Capture print outputs
            old_stdout = sys.stdout
            sys.stdout = io.StringIO()

            try:
                # Run the backtest
                run_backtest(initial_cash, start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"))
                
                # Get the captured output
                output = sys.stdout.getvalue()

                # Display the results
                st.subheader("Backtest Results")
                st.text(output)

                # You might need to modify your run_backtest function to return the figure
                # instead of plotting it directly. Then you can display it like this:
                # fig = run_backtest(...)  # Modified to return the figure
                # st.pyplot(fig)

            except Exception as e:
                st.error(f"An error occurred: {e}")
            finally:
                # Restore stdout
                sys.stdout = old_stdout

if __name__ == "__main__":
    main()