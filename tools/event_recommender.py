"""Tool 2: Campus Event Recommender - Find events that match your interests."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are a campus events advisor helping students discover opportunities.

Event categories:
- Academic (lectures, workshops, career fairs)
- Social (mixers, parties, game nights)
- Cultural (performances, exhibitions, celebrations)
- Athletic (games, tournaments, fitness)
- Professional (networking, panels, info sessions)
- Wellness (meditation, health fairs, support groups)"""

def run():
    console.print("[bold cyan]🎉 Campus Event Recommender[/bold cyan]")
    console.print("[dim]Find events that match your interests[/dim]\n")
    
    mode = Prompt.ask(
        "[green]What would you like?[/green]",
        choices=["find-events", "plan-week", "event-types", "networking-events"],
        default="find-events"
    )
    
    if mode == "find-events":
        interests = Prompt.ask("[green]Your interests (comma-separated)[/green]")
        event_mood = Prompt.ask("[green]What are you looking for?[/green]",
                               choices=["social", "professional", "cultural", "relaxing", "active", "any"],
                               default="any")
        
        prompt = f"""Recommend campus events:

Interests: {interests}
Mood: {event_mood}

Provide:
1. 🎯 TOP RECOMMENDATIONS
   For each (5-7 events):
   - Event type
   - Why you'd enjoy it
   - What to expect
   - How to prepare

2. 📅 TIMING SUGGESTIONS
   - Best times to attend events
   - Recurring vs one-time

3. 👥 SOCIAL TIPS
   - How to meet people
   - Conversation starters

4. 💡 HIDDEN OPPORTUNITIES
   - Lesser-known events
   - Unique experiences"""

    elif mode == "plan-week":
        console.print("\n[yellow]Describe your schedule and preferences:[/yellow]")
        preferences = get_multiline_input("Enter info (type 'END' when done):")
        
        prompt = f"""Plan a week of campus events:

Preferences: {preferences}

Create:
1. 📅 WEEKLY EVENT SCHEDULE
   Monday: [suggestion]
   Tuesday: [suggestion]
   ...

2. ⚖️ BALANCE
   - Academic events
   - Social events
   - Wellness events

3. 💡 FLEXIBILITY TIPS
   - Drop-in options
   - Low-commitment events"""

    elif mode == "event-types":
        prompt = """Explain campus event types:

1. 📚 ACADEMIC EVENTS
   - Types and examples
   - Benefits

2. 🎭 CULTURAL EVENTS
   - Types and examples
   - What to expect

3. 💼 PROFESSIONAL EVENTS
   - Types and examples
   - How to prepare

4. 🎉 SOCIAL EVENTS
   - Types and examples
   - Meeting people tips

5. 🧘 WELLNESS EVENTS
   - Types and examples
   - Benefits"""

    else:  # networking-events
        goals = Prompt.ask("[green]Your networking goals[/green]")
        
        prompt = f"""Find networking opportunities:

Goals: {goals}

Provide:
1. 🎯 EVENT TYPES
   - Best events for networking
   - What each offers

2. 💬 PREPARATION
   - Before the event
   - Elevator pitch tips

3. 🤝 DURING THE EVENT
   - Approaching people
   - Meaningful conversations

4. 📧 FOLLOW-UP
   - After the event
   - Building relationships"""

    console.print("\n[yellow]Finding events...[/yellow]\n")
    result = chat(prompt, SYSTEM_PROMPT)
    display_result("🎉 Event Recommendations", result, "magenta")

if __name__ == "__main__":
    run()
