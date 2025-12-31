"""Tool 12: Student Budget Advisor - Manage student finances effectively."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are a financial advisor specializing in student finances.

Areas:
- Budgeting basics
- Managing limited income
- Reducing expenses
- Student discounts
- Emergency funds
- Part-time work balance
- Financial aid optimization"""

def run():
    console.print("[bold cyan]💰 Student Budget Advisor[/bold cyan]")
    console.print("[dim]Manage your student finances effectively[/dim]\n")
    
    mode = Prompt.ask(
        "[green]What would you like?[/green]",
        choices=["create-budget", "reduce-expenses", "find-income", "emergency-fund"],
        default="create-budget"
    )
    
    if mode == "create-budget":
        income = Prompt.ask("[green]Monthly income (including aid)[/green]", default="$1000")
        
        console.print("\n[dim]List your regular expenses:[/dim]")
        expenses = get_multiline_input("Enter expenses (type 'END' when done):")
        
        prompt = f"""Create student budget:

Income: {income}/month
Current expenses: {expenses}

Provide:
1. 📊 BUDGET BREAKDOWN
   - Essential expenses
   - Variable expenses
   - Savings goal

2. 💵 ALLOCATION
   - 50/30/20 adapted for students
   - Category percentages

3. 📱 TRACKING SYSTEM
   - How to track spending
   - Apps and tools

4. 💡 SAVINGS OPPORTUNITIES
   - Where to cut
   - Student discounts

5. ⚠️ WARNING SIGNS
   - Overspending indicators"""

    elif mode == "reduce-expenses":
        console.print("\n[yellow]List your current expenses:[/yellow]")
        expenses = get_multiline_input("Enter expenses (type 'END' when done):")
        
        prompt = f"""Reduce student expenses:

Current: {expenses}

Provide:
1. 🎯 QUICK WINS
   - Immediate savings
   - Easy cuts

2. 📚 TEXTBOOK SAVINGS
   - Free alternatives
   - Rental options

3. 🍽️ FOOD SAVINGS
   - Meal planning
   - Campus deals

4. 🎉 ENTERTAINMENT
   - Free activities
   - Student discounts

5. 💡 HIDDEN SAVINGS
   - Often overlooked"""

    elif mode == "find-income":
        availability = Prompt.ask("[green]Hours available for work[/green]", default="10-15")
        skills = Prompt.ask("[green]Your skills[/green]", default="general")
        
        prompt = f"""Find student income sources:

Available: {availability} hours/week
Skills: {skills}

Provide:
1. 💼 ON-CAMPUS JOBS
   - Best options
   - How to find them

2. 💻 ONLINE INCOME
   - Freelancing
   - Remote opportunities

3. 🎓 ACADEMIC INCOME
   - Tutoring
   - Research assistant

4. 💵 PASSIVE INCOME
   - Ideas for students

5. 📋 APPLICATION TIPS
   - Standing out"""

    else:  # emergency-fund
        prompt = """Build student emergency fund:

1. 🎯 TARGET AMOUNT
   - Starter goal
   - Full goal

2. 💰 SAVINGS STRATEGIES
   - Small amounts
   - Windfalls

3. 🏦 WHERE TO KEEP IT
   - Account types
   - Accessibility

4. ⚠️ WHAT'S AN EMERGENCY
   - Use it for
   - Don't use for

5. 🔄 REBUILDING
   - After using it"""

    console.print("\n[yellow]Calculating...[/yellow]\n")
    result = chat(prompt, SYSTEM_PROMPT)
    display_result("💰 Budget Advice", result, "yellow")

if __name__ == "__main__":
    run()
