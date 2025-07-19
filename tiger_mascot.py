import random
from typing import Dict, List

class TigerMascot:
    """Animated tiger mascot that reacts to chat interactions"""
    
    def __init__(self):
        """Initialize the tiger mascot with different states and animations"""
        
        # Different tiger emojis and expressions
        self.tiger_emojis = {
            "idle": ["🐅", "🐯", "🦁"],
            "thinking": ["🐅💭", "🤔🐯", "💭🦁"],
            "happy": ["😊🐅", "😄🐯", "🥳🦁", "😸🐅"],
            "excited": ["🤩🐅", "⭐🐯", "✨🦁", "🎉🐅"],
            "sad": ["😢🐅", "😔🐯", "😿🦁"],
            "confused": ["😵🐅", "🤯🐯", "😖🦁", "🙃🐅"],
            "celebrating": ["🎉🐅", "🎊🐯", "🏆🦁", "🥳🐅"]
        }
        
        # Animation classes for different states
        self.animations = {
            "idle": ["pulse"],
            "thinking": ["spin"],
            "happy": ["bounce"],
            "excited": ["shake", "bounce"],
            "sad": [""],
            "confused": ["shake"],
            "celebrating": ["bounce", "spin"]
        }
        
        # Reaction phrases for different contexts
        self.reactions = {
            "greeting": [
                "Roar! Hello there! 🐅",
                "Greetings, human friend! 🐯",
                "*Tiger purrs* Welcome! 😸🐅"
            ],
            "thinking": [
                "Let me think about this... 🤔",
                "*Tiger contemplates* Hmm... 💭",
                "Processing your question... ⚡"
            ],
            "success": [
                "Roar! Great response! 🎉",
                "*Happy tiger noises* 😄",
                "Purr-fect answer! 🐾"
            ],
            "error": [
                "*Confused tiger sounds* 😵",
                "Oops! Something went wrong... 😔",
                "*Tiger looks puzzled* 🤔"
            ]
        }
    
    def get_tiger_emoji(self, state: str) -> str:
        """
        Get a tiger emoji for the given state
        
        Args:
            state: Current state of the tiger (idle, thinking, happy, etc.)
            
        Returns:
            Tiger emoji string for the state
        """
        if state in self.tiger_emojis:
            return random.choice(self.tiger_emojis[state])
        else:
            return random.choice(self.tiger_emojis["idle"])
    
    def get_animation_class(self, state: str) -> str:
        """
        Get CSS animation class for the given state
        
        Args:
            state: Current state of the tiger
            
        Returns:
            CSS animation class name
        """
        if state in self.animations:
            return random.choice(self.animations[state])
        else:
            return random.choice(self.animations["idle"])
    
    def get_reaction_phrase(self, context: str) -> str:
        """
        Get a reaction phrase for the given context
        
        Args:
            context: Context of the reaction (greeting, thinking, success, error)
            
        Returns:
            Reaction phrase string
        """
        if context in self.reactions:
            return random.choice(self.reactions[context])
        else:
            return "🐅 *Tiger makes friendly sounds*"
    
    def get_state_description(self, state: str) -> str:
        """
        Get description of what the tiger is doing in the given state
        
        Args:
            state: Current state of the tiger
            
        Returns:
            Description string of the tiger's current state
        """
        descriptions = {
            "idle": "Tiger is relaxing and waiting for your message",
            "thinking": "Tiger is thinking hard about your question",
            "happy": "Tiger is happy and satisfied with the response",
            "excited": "Tiger is excited and ready to help",
            "sad": "Tiger is sad because something went wrong",
            "confused": "Tiger is confused and needs a moment",
            "celebrating": "Tiger is celebrating a successful interaction"
        }
        
        return descriptions.get(state, "Tiger is in an unknown state")
    
    def determine_reaction_state(self, message_content: str, is_error: bool = False) -> str:
        """
        Determine the appropriate tiger state based on message content and context
        
        Args:
            message_content: The content of the AI response
            is_error: Whether an error occurred
            
        Returns:
            Appropriate state for the tiger
        """
        if is_error:
            return "sad"
        
        # Convert to lowercase for easier matching
        content_lower = message_content.lower()
        
        # Check for greeting patterns
        greeting_words = ["hello", "hi", "hey", "greetings", "welcome", "namaste"]
        if any(word in content_lower for word in greeting_words):
            return "excited"
        
        # Check for positive sentiment
        positive_words = ["great", "excellent", "wonderful", "amazing", "fantastic", "good", "yes", "correct"]
        if any(word in content_lower for word in positive_words):
            return "happy"
        
        # Check for questions or complex responses
        question_indicators = ["?", "what", "how", "why", "when", "where", "which"]
        if any(indicator in content_lower for indicator in question_indicators):
            return "thinking"
        
        # Check for celebration-worthy content
        celebration_words = ["congratulations", "success", "achievement", "won", "victory", "celebrate"]
        if any(word in content_lower for word in celebration_words):
            return "celebrating"
        
        # Default to happy state for normal responses
        return "happy"
    
    def get_context_appropriate_emoji(self, user_message: str, ai_response: str) -> str:
        """
        Get contextually appropriate tiger emoji based on conversation
        
        Args:
            user_message: The user's input message
            ai_response: The AI's response message
            
        Returns:
            Contextually appropriate tiger emoji
        """
        # Determine state based on the conversation
        state = self.determine_reaction_state(ai_response)
        
        # Get emoji for that state
        return self.get_tiger_emoji(state)
    
    def get_tiger_status_html(self, state: str) -> str:
        """
        Generate HTML for tiger status display
        
        Args:
            state: Current tiger state
            
        Returns:
            HTML string for tiger status
        """
        emoji = self.get_tiger_emoji(state)
        description = self.get_state_description(state)
        animation = self.get_animation_class(state)
        
        html = f"""
        <div style="
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 0.5rem;
            background: rgba(255, 107, 53, 0.1);
            border-radius: 10px;
            margin: 0.5rem 0;
        ">
            <span class="tiger-mascot {animation}" style="font-size: 2rem; margin-right: 0.5rem;">
                {emoji}
            </span>
            <span style="font-size: 0.9rem; font-style: italic;">
                {description}
            </span>
        </div>
        """
        
        return html
    
    def get_random_idle_animation(self) -> str:
        """
        Get a random idle animation for the tiger when no interaction is happening
        
        Returns:
            Random idle animation class
        """
        idle_animations = ["pulse", "", ""]  # Empty strings for no animation
        return random.choice(idle_animations)
    
    def create_tiger_greeting(self) -> Dict[str, str]:
        """
        Create a greeting message from the tiger mascot
        
        Returns:
            Dictionary with tiger emoji, message, and animation
        """
        greeting_messages = [
            "Hello! I'm your friendly AI chat tiger! 🐅",
            "Roar! Ready to chat and learn together! 🐯",
            "Greetings! Your tiger companion is here to help! 🦁",
            "*Tiger waves paw* Let's have an amazing conversation! 🐾"
        ]
        
        return {
            "emoji": random.choice(self.tiger_emojis["excited"]),
            "message": random.choice(greeting_messages),
            "animation": random.choice(self.animations["excited"]),
            "state": "excited"
        }
