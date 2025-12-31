"""Tool 9: Meal Plan Optimization Tool - Make the most of your meal plan."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are a campus dining and nutrition expert.

Consider:
- Meal plan types and swipes
- Dining dollar strategies
- Nutrition balance
- Budget optimization
- Schedule compatibility
- Dietary restrictions"""

def run():
    console.print("[bold cyan]🍽️ Meal Plan Optimization Tool[/bold cyan]")
    console.print("[dim]Make the most of your meal plan[/dim]\n")
    
    mode = Prompt.ask(
        "[green]What would you like?[/green]",
        choices=["optimize-plan", "budget-meals", "healthy-eating", "choose-plan"],
        default="optimize-plan"
    )
    
    if mode == "optimize-plan":
        plan_type = Prompt.ask("[green]Your meal plan type[/green]", default="unlimited swipes")
        dietary = Prompt.ask("[green]Dietary restrictions[/green]", default="none")
        
        prompt = f"""Optimize meal plan usage:

Plan: {plan_type}
Dietary needs: {dietary}

Provide:
1. 📊 USAGE STRATEGY
   - When to use swipes
   - When to use dining dollars

2. 🍽️ MEAL TIMING
   - Best times to eat
   - Avoiding rushes

3. 💰 VALUE MAXIMIZATION
   - High-value items
   - Getting your money's worth

4. 🥗 NUTRITION BALANCE
   - Building balanced meals
   - Campus dining options

5. 💡 PRO TIPS
   - Hidden perks
   - Insider strategies"""

    elif mode == "budget-meals":
        budget = Prompt.ask("[green]Weekly food budget[/green]", default="$50")
        
        prompt = f"""Budget meal planning:

Budget: {budget}/week

Provide:
1. 💰 BUDGET BREAKDOWN
   - Dining hall meals
   - Snacks and extras

2. 🛒 GROCERY STRATEGIES
   - What to buy
   - Where to shop

3. 🍳 EASY RECIPES
   - Dorm-friendly meals
   - Quick options

4. 💡 MONEY-SAVING TIPS
   - Campus deals
   - Free food opportunities"""

    elif mode == "healthy-eating":
        console.print("\n[dim]Describe your dining options:[/dim]")
        options = get_multiline_input("Enter options (type 'END' when done):")
        
        prompt = f"""Healthy campus eating guide:

Available: {options}

Provide:
1. 🥗 HEALTHY CHOICES
   - Best options
   - Nutrient-rich picks

2. 🍽️ BALANCED MEALS
   - Building plates
   - Portion guidance

3. ⚠️ AVOID
   - Common pitfalls

4. 💪 ENERGY FOODS
   - For studying
   - For exercise"""

    else:  # choose-plan
        prompt = """Choose the right meal plan:

1. 📊 PLAN TYPES
   - Unlimited
   - Block plans
   - Declining balance

2. 🎯 BEST FOR YOU IF...
   - Scenarios for each

3. 💰 COST ANALYSIS
   - Per-meal costs
   - Value comparison

4. 💡 DECISION GUIDE
   - Questions to ask"""

    console.print("\n[yellow]Optimizing...[/yellow]\n")
    result = chat(prompt, SYSTEM_PROMPT)
    display_result("🍽️ Meal Plan", result, "yellow")

if __name__ == "__main__":
    run()
