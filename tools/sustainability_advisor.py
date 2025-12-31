"""Tool 15: Campus Sustainability Advisor - Live sustainably on campus."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are a campus sustainability expert helping students live eco-friendly.

Areas:
- Reducing waste
- Energy conservation
- Sustainable transportation
- Eco-friendly shopping
- Food sustainability
- Campus initiatives"""

def run():
    console.print("[bold cyan]🌱 Campus Sustainability Advisor[/bold cyan]")
    console.print("[dim]Live sustainably on campus[/dim]\n")
    
    mode = Prompt.ask(
        "[green]What would you like?[/green]",
        choices=["sustainable-living", "reduce-waste", "get-involved", "eco-audit"],
        default="sustainable-living"
    )
    
    if mode == "sustainable-living":
        living_situation = Prompt.ask("[green]Living situation[/green]",
                                     choices=["dorm", "apartment", "off-campus"],
                                     default="dorm")
        
        prompt = f"""Sustainable campus living ({living_situation}):

Provide:
1. 🌱 DAILY HABITS
   - Morning to night
   - Easy swaps

2. 🚿 RESOURCE CONSERVATION
   - Water saving
   - Energy saving

3. 🛒 SUSTAINABLE SHOPPING
   - What to buy
   - Where to shop

4. 🍽️ FOOD CHOICES
   - Sustainable eating
   - Reducing food waste

5. 🚲 TRANSPORTATION
   - Getting around green

6. 📦 WASTE REDUCTION
   - Reduce, reuse, recycle"""

    elif mode == "reduce-waste":
        prompt = """Reduce waste on campus:

1. ♻️ RECYCLING RIGHT
   - What goes where
   - Common mistakes

2. 🚯 SINGLE-USE SWAPS
   - Bottles and bags
   - Food containers

3. 📚 ACADEMIC WASTE
   - Digital notes
   - Sustainable supplies

4. 👕 CLOTHING
   - Thrift and swap
   - Quality over quantity

5. 🎉 EVENT WASTE
   - Party sustainably

6. 💡 UPCYCLING IDEAS
   - Creative reuse"""

    elif mode == "get-involved":
        prompt = """Get involved in campus sustainability:

1. 🌍 CAMPUS GROUPS
   - Environmental clubs
   - Advocacy organizations

2. 🎯 INITIATIVES
   - Campaigns to join
   - Projects to start

3. 💼 JOBS & INTERNSHIPS
   - Green campus jobs
   - Sustainability internships

4. 📢 ADVOCACY
   - Making change
   - Working with administration

5. 🎓 ACADEMIC CONNECTIONS
   - Sustainability courses
   - Research opportunities"""

    else:  # eco-audit
        console.print("\n[yellow]Describe your current habits:[/yellow]")
        habits = get_multiline_input("Enter habits (type 'END' when done):")
        
        prompt = f"""Eco-audit your lifestyle:

Current: {habits}

Provide:
1. 📊 IMPACT ASSESSMENT
   - Current footprint
   - Main impacts

2. ✅ GREEN HABITS
   - What you're doing well

3. 🎯 IMPROVEMENT AREAS
   - Priority changes
   - Easy wins

4. 📋 ACTION PLAN
   - This week
   - This month
   - This semester

5. 📈 TRACKING PROGRESS
   - How to measure"""

    console.print("\n[yellow]Processing...[/yellow]\n")
    result = chat(prompt, SYSTEM_PROMPT)
    display_result("🌱 Sustainability Guide", result, "green")

if __name__ == "__main__":
    run()
