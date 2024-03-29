import time
import streamlit as st
import re
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns
from collections import Counter
import emoji
from wordcloud import WordCloud
from urlextract import URLExtract
from PIL import Image

extract = URLExtract()

stop_words=[
    ".",
    "..",
    "...",
    "?",
    "-",
    "--",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
    "a",
    "aadi",
    "aaj",
    "aap",
    "aapne",
    "aata",
    "aati",
    "aaya",
    "aaye",
    "ab",
    "abbe",
    "abbey",
    "abe",
    "abhi",
    "able",
    "about",
    "above",
    "accha",
    "according",
    "accordingly",
    "acha",
    "achcha",
    "across",
    "actually",
    "after",
    "afterwards",
    "again",
    "against",
    "agar",
    "ain",
    "aint",
    "ain't",
    "aisa",
    "aise",
    "aisi",
    "alag",
    "all",
    "allow",
    "allows",
    "almost",
    "alone",
    "along",
    "already",
    "also",
    "although",
    "always",
    "am",
    "among",
    "amongst",
    "an",
    "and",
    "andar",
    "another",
    "any",
    "anybody",
    "anyhow",
    "anyone",
    "anything",
    "anyway",
    "anyways",
    "anywhere",
    "ap",
    "apan",
    "apart",
    "apna",
    "apnaa",
    "apne",
    "apni",
    "appear",
    "are",
    "aren",
    "arent",
    "aren't",
    "around",
    "arre",
    "as",
    "aside",
    "ask",
    "asking",
    "at",
    "aur",
    "avum",
    "aya",
    "aye",
    "baad",
    "baar",
    "bad",
    "bahut",
    "bana",
    "banae",
    "banai",
    "banao",
    "banaya",
    "banaye",
    "banayi",
    "banda",
    "bande",
    "bandi",
    "bane",
    "bani",
    "bas",
    "bata",
    "batao",
    "bc",
    "be",
    "became",
    "because",
    "become",
    "becomes",
    "becoming",
    "been",
    "before",
    "beforehand",
    "behind",
    "being",
    "below",
    "beside",
    "besides",
    "best",
    "better",
    "between",
    "beyond",
    "bhai",
    "bheetar",
    "bhi",
    "bhitar",
    "bht",
    "bilkul",
    "bohot",
    "bol",
    "bola",
    "bole",
    "boli",
    "bolo",
    "bolta",
    "bolte",
    "bolti",
    "both",
    "brief",
    "bro",
    "btw",
    "but",
    "by",
    "came",
    "can",
    "cannot",
    "cant",
    "can't",
    "cause",
    "causes",
    "certain",
    "certainly",
    "chahiye",
    "chaiye",
    "chal",
    "chalega",
    "chhaiye",
    "clearly",
    "c'mon",
"com",
    "come",
    "comes",
    "could",
    "couldn",
    "couldnt",
    "couldn't",
    "d",
    "de",
    "dede",
    "dega",
    "degi",
    "dekh",
    "dekha",
    "dekhe",
    "dekhi",
    "dekho",
    "denge",
    "dhang",
    "di",
    "did",
    "didn",
    "didnt",
    "didn't",
    "dijiye",
    "diya",
    "diyaa",
    "diye",
    "diyo",
    "do",
    "does",
    "doesn",
    "doesnt",
    "doesn't",
    "doing",
    "done",
    "dono",
    "dont",
    "don't",
    "doosra",
    "doosre",
    "down",
    "downwards",
    "dude",
    "dunga",
    "dungi",
    "during",
    "dusra",
    "dusre",
    "dusri",
    "dvaara",
    "dvara",
    "dwaara",
    "dwara",
    "each",
    "edu",
    "eg",
    "eight",
    "either",
    "ek",
    "else",
    "elsewhere",
    "enough",
    "etc",
    "even",
    "ever",
    "every",
    "everybody",
    "everyone",
    "everything",
    "everywhere",
    "ex",
    "exactly",
    "example",
    "except",
    "far",
    "few",
    "fifth",
    "fir",
    "first",
    "five",
    "followed",
    "following",
    "follows",
    "for",
    "forth",
    "four",
    "from",
    "further",
    "furthermore",
    "gaya",
    "gaye",
    "gayi",
    "get",
    "gets",
    "getting",
    "ghar",
    "given",
    "gives",
    "go",
    "goes",
    "going",
    "gone",
    "good",
    "got",
    "gotten",
    "greetings",
    "guys",
    "haan",
    "had",
    "hadd",
    "hadn",
    "hadnt",
    "hadn't",
    "hai",
    "hain",
    "hamara",
    "hamare",
    "hamari",
    "hamne",
    "han",
    "happens",
    "har",
    "hardly",
    "has",
    "hasn",
    "hasnt",
    "hasn't",
    "have",
    "haven",
    "havent",
    "haven't",
    "having",
    "he",
    "hello",
    "help",
    "hence",
    "her",
    "here",
    "hereafter",
    "hereby",
    "herein",
    "here's",
    "hereupon",
    "hers",
    "herself",
    "he's",
    "hi",
    "him",
    "himself",
    "his",
    "hither",
    "hm",
 "hmm",
    "ho",
    "hoga",
    "hoge",
    "hogi",
    "hona",
    "honaa",
    "hone",
    "honge",
    "hongi",
    "honi",
    "hopefully",
    "hota",
    "hotaa",
    "hote",
    "hoti",
    "how",
    "howbeit",
    "however",
    "hoyenge",
    "hoyengi",
    "hu",
    "hua",
    "hue",
    "huh",
    "hui",
    "hum",
    "humein",
    "humne",
    "hun",
    "huye",
    "huyi",
    "i",
    "i'd",
    "idk",
    "ie",
    "if",
    "i'll",
    "i'm",
    "imo",
    "in",
    "inasmuch",
    "inc",
    "inhe",
    "inhi",
    "inho",
    "inka",
    "inkaa",
    "inke",
    "inki",
    "inn",
    "inner",
    "inse",
    "insofar",
    "into",
    "inward",
    "is",
    "ise",
    "isi",
    "iska",
    "iskaa",
    "iske",
    "iski",
    "isme",
    "isn",
    "isne",
    "isnt",
    "isn't",
    "iss",
    "isse",
    "issi",
    "isski",
    "it",
    "it'd",
    "it'll",
    "itna",
    "itne",
    "itni",
    "itno",
    "its",
    "it's",
    "itself",
    "ityaadi",
    "ityadi",
    "i've",
    "ja",
    "jaa",
    "jab",
    "jabh",
    "jaha",
    "jahaan",
    "jahan",
    "jaisa",
    "jaise",
    "jaisi",
    "jata",
    "jayega",
    "jidhar",
    "jin",
    "jinhe",
    "jinhi",
    "jinho",
    "jinhone",
    "jinka",
    "jinke",
    "jinki",
    "jinn",
    "jis",
    "jise",
    "jiska",
    "jis",
"jise",
    "jiska",
    "jiski",
    "jiski",
    "jisme",
    "jiss",
    "jisse",
    "jitna",
    "jitne",
    "jitni",
    "jo",
    "just",
    "jyaada",
    "jyada",
    "k",
    "ka",
    "kaafi",
    "kab",
    "kabhi",
    "kafi",
    "kaha",
    "kahaa",
    "kahaan",
    "kahan",
    "kahi",
    "kahin",
    "kahte",
    "kaisa",
    "kaise",
    "kaisi",
    "kal",
    "kam",
    "kar",
    "kara",
    "kare",
    "karega",
    "karegi",
    "karen",
    "karenge",
    "kari",
    "karke",
    "karna",
    "karne",
    "karni",
    "karo",
    "karta",
    "karte",
    "karti",
    "karu",
    "karun",
    "karunga",
    "karungi",
    "kaun",
    "kaunsa",
    "kayi",
    "kch",
    "ke",
    "keep",
    "keeps",
    "keh",
    "kehte",
    "kept",
    "khud",
    "ki",
    "kin",
    "kine",
    "kinhe",
    "kinho",
    "kinka",
    "kinke",
    "kinki",
    "kinko",
    "kinn",
    "kino",
    "kis",
    "kise",
    "kisi",
    "kiska",
    "kiske",
    "kiski",
    "kisko",
    "kisliye",
    "kisne",
    "kitna",
    "kitne",
    "kitni",
    "kitno",
    "kiya",
    "kiye",
    "know",
    "known",
    "knows",
    "ko",
    "koi",
    "kon",
    "konsa",
    "koyi",
    "krna",
    "krne",
    "kuch",
    "kuchch",
    "kuchh",
    "kul",
    "kull",
    "kya",
    "kyaa",
    "kyu",
    "kyuki",
    "kyun",
    "kyunki",
    "lagta",
    "lagte",
    "lagti",
    "last",
    "lately",
    "later",
    "le",
    "least",
    "lekar",
    "lekin",
    "less",
    "lest",
    "let",
    "let's",
    "li",
    "like",
    "liked",
    "likely",
    "little",
    "liya",
    "liye",
    "ll",
    "lo",
    "log",
    "logon",
    "lol",
    "look",
    "looking",
    "looks",
    "ltd",
    "lunga",
    "m",
    "maan",
    "maana",
    "maane",
    "maani",
    "maano",
    "magar",
    "mai",
    "main",
    "maine",
    "mainly",
    "mana",
    "mane",
    "mani",
    "mano",
    "many",
    "mat",
    "may",
    "maybe",
    "me",
    "mean",
    "meanwhile",
    "mein",
    "mera",
    "mere",
    "merely",
    "meri",
    "might",
    "mightn",
    "mightnt",
    "mightn't",
    "mil",
    "mjhe",
    "more",
    "moreover",
    "most",
    "mostly",
    "much",
    "mujhe",
    "must",
    "mustn",
    "mustnt",
    "mustn't",
    "my",
    "myself",
    "na",
    "naa",
    "naah",
    "nahi",
    "nahin",
    "nai",
    "name",
    "namely",
    "nd",
    "ne",
    "near",
    "nearly",
    "necessary",
    "neeche",
    "need",
    "needn",
    "neednt",
    "needn't",
    "needs",
    "neither",
"never",
    "nevertheless",
    "new",
    "next",
    "nhi",
    "nine",
    "no",
    "nobody",
    "non",
    "none",
    "noone",
    "nope",
    "nor",
    "normally",
    "not",
    "nothing",
    "novel",
    "now",
    "nowhere",
    "o",
    "obviously",
    "of",
    "off",
    "often",
    "oh",
    "ok",
    "okay",
    "old",
    "on",
    "once",
    "one",
    "ones",
    "only",
    "onto",
    "or",
    "other",
    "others",
    "otherwise",
    "ought",
    "our",
    "ours",
    "ourselves",
    "out",
    "outside",
    "over",
    "overall",
    "own",
    "par",
    "pata",
    "pe",
    "pehla",
    "pehle",
    "pehli",
    "people",
    "per",
    "perhaps",
    "phla",
    "phle",
    "phli",
    "placed",
    "please",
    "plus",
    "poora",
    "poori",
    "provides",
    "pura",
    "puri",
    "q",
    "que",
    "quite",
    "raha",
    "rahaa",
    "rahe",
    "rahi",
    "rakh",
    "rakha",
    "rakhe",
    "rakhen",
    "rakhi",
    "rakho",
    "rather",
    "re",
    "really",
    "reasonably",
    "regarding",
    "regardless",
    "regards",
    "rehte",
    "rha",
    "rhaa",
    "rhe",
    "rhi",
    "ri",
    "right",
    "s",
    "sa",
    "saara",
    "saare",
    "saath",
    "sab",
    "sabhi",
    "sabse",
    "sahi",
    "said",
    "sakta",
    "saktaa",
    "sakte",
    "sakti",
    "same",
    "sang",
    "sara",
"sath",
    "saw",
    "say",
    "saying",
    "says",
    "se",
    "second",
    "secondly",
    "see",
    "seeing",
    "seem",
    "seemed",
    "seeming",
    "seems",
    "seen",
    "self",
    "selves",
    "sensible",
    "sent",
    "serious",
    "seriously",
    "seven",
    "several",
    "shall",
    "shan",
    "shant",
    "shan't",
    "she",
    "she's",
    "should",
    "shouldn",
    "shouldnt",
    "shouldn't",
    "should've",
    "si",
    "sir",
    "sir.",
    "since",
    "six",
    "so",
    "soch",
    "some",
    "somebody",
    "somehow",
    "someone",
    "something",
    "sometime",
    "sometimes",
    "somewhat",
    "somewhere",
    "soon",
    "still",
    "sub",
    "such",
    "sup",
    "sure",
    "t",
    "tab",
    "tabh",
    "tak",
    "take",
    "taken",
    "tarah",
    "teen",
    "teeno",
    "teesra",
    "teesre",
    "teesri",
    "tell",
    "tends",
    "tera",
    "tere",
    "teri",
    "th",
    "tha",
    "than",
    "thank",
    "thanks",
    "thanx",
    "that",
    "that'll",
    "thats",
    "that's",
    "the",
    "theek",
    "their",
    "theirs",
    "them",
    "themselves",
    "then",
    "thence",
    "there",
    "thereafter",
    "thereby",
    "therefore",
    "therein",
    "theres",
    "there's",
    "thereupon",
    "these",
    "they",
    "they'd",
    "they'll",
    "they're",
    "they've",
    "thi",
    "thik",
    "thing",
    "think",
    "thinking",
    "third",
    "this",
    "tho",
    "thoda",
    "thodi",
    "thorough",
    "thoroughly",
    "those",
    "though",
    "thought",
    "three",
    "through",
    "throughout",
    "thru",
    "thus",
    "tjhe",
    "to",
    "together",
    "toh",
    "too",
    "took",
    "toward",
    "towards",
    "tried",
    "tries",
    "true",
    "truly",
    "try",
    "trying",
    "tu",
    "tujhe",
    "tum",
    "tumhara",
    "tumhare",
    "tumhari",
    "tune",
    "twice",
    "two",
    "um",
    "umm",
    "un",
    "under",
    "unhe",
    "unhi",
    "unho",
    "unhone",
    "unka",
    "unkaa",
    "unke",
    "unki",
    "unko",
    "unless",
    "unlikely",
    "unn",
    "unse",
    "until",
    "unto",
    "up",
    "upar",
    "upon",
    "us",
    "use",
    "used",
    "useful",
    "uses",
    "usi",
    "using",
    "uska",
    "uske",
    "usne",
    "uss",
    "usse",
    "ussi",
    "usually",
    "vaala",
    "vaale",
    "vaali",
    "vahaan",
    "vahan",
    "vahi",
    "vahin",
    "vaisa",
    "vaise",
    "vaisi",
    "vala",
    "vale",
    "vali",
    "various",
    "ve",
    "very",
    "via",
    "viz",
    "vo",
    "waala",
    "waale",
    "waali",
    "wagaira",
    "wagairah",
    "wagerah",
    "waha",
    "wahaan",
    "wahan",
    "wahi",
    "wahin",
    "waisa",
    "waise",
    "waisi",
    "wala",
    "wale",
    "wali",
    "want",
    "wants",
    "was",
    "wasn",
    "wasnt",
    "wasn't",
    "way",
    "we",
    "we'd",
    "well",
"we'll",
    "went",
    "were",
    "we're",
    "weren",
    "werent",
    "weren't",
    "we've",
    "what",
    "whatever",
    "what's",
    "when",
    "whence",
    "whenever",
    "where",
    "whereafter",
    "whereas",
    "whereby",
    "wherein",
    "where's",
    "whereupon",
    "wherever",
    "whether",
    "which",
    "while",
    "who",
    "whoever",
    "whole",
    "whom",
    "who's",
    "whose",
    "why",
    "will",
    "willing",
    "with",
    "within",
    "without",
    "wo",
    "woh",
    "wohi",
    "won",
    "wont",
    "won't",
    "would",
    "wouldn",
    "wouldnt",
    "wouldn't",
    "y",
    "ya",
    "yadi",
    "yah",
    "yaha",
    "yahaan",
    "yahan",
    "yahi",
    "yahin",
    "ye",
    "yeah",
    "yeh",
    "yehi",
    "yes",
    "yet",
    "you",
    "you'd",
    "you'll",
    "your",
    "you're",
    "yours",
    "yourself",
    "yourselves",
    "you've",
    "yup"
]

def preprocess(data):
    message_pattern ='\d{1,2}/\d{1,2}/\d{1,2},\s\d{1,2}:\d{2}\s(?:am|pm)\s-\s' 
    messages = re.split(message_pattern, data)[1:]
    dates = re.findall(message_pattern, data)
    df = pd.DataFrame({'user_message': messages, 'message_date': dates})
    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %I:%M %p - ')  
    df.rename(columns={'message_date': 'date'}, inplace=True)
    users = []
    messages = []

    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)
    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute
    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour)+ "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour+1))
        else:
            period.append(str(hour)+ "-" + str(hour+1))
    df['period'] = period

    return df

def fetch_stats(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    num_messages = df.shape[0]
    words = []
    for message in df['message']:
        words.extend(message.split())

    num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]
    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message) or [])

    return num_messages, len(words), num_media_messages, len(links)

def most_busy_users(df):
    x = df['user'].value_counts().head()
    df = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(columns={'index': 'name', 'user': 'percent'})

    return x, df

def create_wordcloud(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted\n>']
    def remove_stop_words(message):
        y = []
        for word in message.lower().split():
            if word not in stop_words:
                y.append(word)
        return " ".join(y)
    wc = WordCloud(width=500,height=500,min_font_size=10,background_color='white')
    temp['message'] = temp['message'].apply(remove_stop_words)
    df_wc = wc.generate(temp['message'].str.cat(sep=" "))
    return df_wc

def most_common_words(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted\n>']
    words = []

    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    most_common_df = pd.DataFrame(Counter(words).most_common(20), columns=['Word', 'Count'])
    return most_common_df

def emoji_helper(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] ==selected_user ]
    emojis = []
    for message in df['message']:
        emojis.extend([c for c in message if c in emoji.EMOJI_DATA]) 

    emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))
    return emoji_df

def monthly_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user']==selected_user]
    timeline = df.groupby(['year','month_num','month']).count()['message'].reset_index()
    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))
    timeline['time'] = time
    return timeline

def daily_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    daily_timeline = df.groupby('only_date').count()['message'].reset_index()
    return daily_timeline

def week_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    return df['day_name'].value_counts()

def month_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    return df['month'].value_counts()

def activity_heatmap(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    user_heatmap = df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)
    return user_heatmap

st.set_page_config(layout="wide")

html_string = '''
<style>
.dotted-line {
  border-top: 2px dashed #999;
  margin-top: 20px;
  margin-bottom: 20px;
  padding-top: 10px;
  padding-bottom: 10px;
}
</style>
<div class="dotted-line"></div>
'''


st.markdown("""
<head>
<title>Font Awesome Icons</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>

<style>
    body {
        background-color: #f4f4f4; /* White background color */
    }
.container {
    min-height: 75vh;
    opacity : 0.9;
    display: flex;
    align-items: center;
    box-sizing: border-box; 
    padding: -10px;
    animation: fadeInBackground 2s ease-in-out;
    justify-content: flex-start;
    border-radius: 20px; /* Rounded edges */
    overflow: hidden; /* Hide overflow content */
    animation: slideDown 2s ease-in-out; /* Dropdown animation */
}
.video-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 20px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.3); /* Add a subtle shadow */
  transition: transform 0.5s ease; /* Add a smooth transition effect */
}

.video-background:hover {
  transform: scale(1.02); /* Slightly scale up on hover */
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.6); /* Slightly darker overlay */
  border-radius: 22px; /* Match the rounded edges of the video */
}
@keyframes slideDown {
    from {
        transform: translateY(-50px);
        opacity: 0;
    }
    to {
        transform: translateY(0);
        opacity: 1;
    }
}
@keyframes fadeInBackground {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}

.content {
    background-color: rgba(255, 255, 255, 0); /* Changed background color to fully transparent */
    padding: 10px;
    margin-top: -10px;
    text-align: left;
    border: none; /* Removed border to eliminate the white lining */
    border-radius: 10px;
    max-width: 1000px;
    display: flex; /* Enable flexbox */
    flex-direction: column; /* Arrange items in a column */
    align-items: flex-start; /* Center items horizontally */
}

.title {
  font-family: 'Helvetica Neue', sans-serif;
  font-size: 60px;
  color: #90EE90; /* Change color to black */
  text-decoration: none;
  margin-top: -20px;
  animation: fadeInTitle 1s ease-in-out 0.5s forwards;
  opacity: 0;
  padding:20px;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

.center {
  display: flex;
  justify-content: flex-start;
  width: 100%;
  margin-top: 20px;
}

.text {
  font-family: Arial, sans-serif;
  font-size: 20px;
  color: #ffff;
  animation: fadeInText 2s ease-in-out 1.5s forwards;
  text-align: left;
  opacity: 0;
  line-height: 1.6;
  padding: 20px;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
}

@keyframes fadeInTitle {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeInText {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
}
.scroll-down {
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    z-index: 1000;
    animation: bounce 2s infinite;
    cursor: pointer;
}

@keyframes bounce {
    0%, 20%, 50%, 80%, 100% {
        transform: translateY(0);
    }
    40% {
        transform: translateY(-10px);
    }
    60% {
        transform: translateY(-5px);
    }
}

.scroll-down i {
    font-size: 24px;
    color: white;
}

.dotted-line {
    border-top: 2px dashed #999; /* Adjust the thickness and color of the dashed line */
    margin-top: 20px;
    margin-bottom: 20px;
    padding-top: 10px; /* Adjust the top padding */
    padding-bottom: 10px; /* Adjust the bottom padding */
}

</style>

<div class="container">
    <video class="video-background" autoplay loop muted>
        <source src="https://pouch.jumpshare.com/preview/GI3JZmXbfqjXKXgXhdG0jPBF91-paFOP5gA5QYnVMs-GT6NrVi8WIp6ecpaL-krC2jkOSNdPzOkYe5AoD-tlgjA5VS1w-5D9r5xX4JIKSGrsM6P7_n6Bi0eo8jJx7ADo5KUXRBZYe9v7JabbUMXvVW6yjbN-I2pg_cnoHs_AmgI.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    <div class="overlay"></div>
    <div class="content">
        <div class="title">WhatsApp Chat Analyzer <i class="fa fa-whatsapp" style="font-size:36px"></i></div>
        <div class="center">
            <div class="text">
                A Streamlit app to analyze your WhatsApp chats with a twist!
            </div>
        </div>
    </div>
</div>

<!-- Scroll down pointer -->
<div class="scroll-down" onclick="scrollToContent()">
    <i class="fa fa-angle-down"></i>
</div>

<script>
function scrollToContent() {
        var contentOffset = document.querySelector('.content').offsetTop;
        window.scrollTo({
            top: contentOffset,
        });
}

</script>

</body>
</html> 
""", unsafe_allow_html=True)

st.markdown("<style>div[data-testid='stSidebar'][aria-expanded='true'] {display: none}</style>", unsafe_allow_html=True)

st.markdown('<div class="center">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Choose a file", key='file_uploader', help='Upload your Whatsapp chat file')

if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        data = bytes_data.decode("utf-8")
        df = preprocess(data)

        # Fetch unique user
        user_list = df['user'].unique().tolist()
        user_list.remove('group_notification')
        user_list.sort()
        user_list.insert(0, "Overall")
        selected_user = st.selectbox("Show analysis wrt", user_list)

        if st.button("Show Analysis"):
            st.empty() 

            with st.spinner("Generating content..."):
                for i in range(7):
                        time.sleep(1)
            
            num_messages, words, num_media_messages, num_links = fetch_stats(selected_user, df)
            st.title("Top Statistics")
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.header("Total Messages")
                st.title(num_messages)
            with col2:
                st.header("Total words")
                st.title(words)
            with col3:
                st.header("Media Shared")
                st.title(num_media_messages)
            with col4:
                st.header("Links Shared")
                st.title(num_links)

            placeholder_others = st.empty()

            st.markdown(html_string, unsafe_allow_html=True)
            
            import matplotlib.animation as animation

            st.title("Monthly Timeline")
            timeline = monthly_timeline(selected_user, df)
            fig, ax = plt.subplots(figsize=(10, 6))
            line, = ax.plot(timeline['time'], timeline['message'], color='green')
            plt.xticks(rotation=45, ha='right')
            ax.set_xlabel("Time")
            ax.set_ylabel("Messages")
            ax.set_title("Monthly Timeline")  
            ax.grid(True, linestyle='--', alpha=0.7)
            ax.patch.set_facecolor('whitesmoke')
            ax.patch.set_alpha(0.9)
            plt.gca().xaxis.set_major_locator(plt.MaxNLocator(10))  
            plt.tight_layout()  

            
            
            placeholder_timeline = st.empty()

            def update_monthly_timeline(frame):
                line.set_data(timeline['time'][:frame], timeline['message'][:frame])
                placeholder_timeline.pyplot(fig)

            ani = animation.FuncAnimation(fig, update_monthly_timeline, frames=len(timeline['time']), interval=50)
            ani.save("monthly_timeline.gif", writer='pillow')
            
            st.markdown('<div class="dotted-line"></div>', unsafe_allow_html=True)
            # Daily timeline
            st.title("Daily Timeline")
            daily_timeline = daily_timeline(selected_user, df)
            fig, ax = plt.subplots(figsize=(10, 6))
            line, = ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='blue', linestyle='-', markersize=4)  # Adjust line style, marker style, and color
            plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels by 45 degrees and align to the right
            plt.gca().xaxis.set_major_locator(plt.MaxNLocator(10))  # Reduce the number of displayed labels
            ax.set_xlabel("Date")
            ax.set_ylabel("Messages")
            ax.set_title("Daily Timeline")
            ax.grid(True, linestyle='--', alpha=0.7)
            ax.patch.set_facecolor('whitesmoke')
            ax.patch.set_alpha(0.9)
            plt.tight_layout()  # Adjust layout for better appearance
            placeholder_daily = st.empty()

            def update_daily_timeline(frame):
                line.set_data(daily_timeline['only_date'][:frame], daily_timeline['message'][:frame])
                placeholder_daily.pyplot(fig)

            ani = animation.FuncAnimation(fig, update_daily_timeline, frames=len(daily_timeline['only_date']), interval=50)
            ani.save("daily_timeline.gif", writer='pillow')

            st.markdown('<div class="dotted-line"></div>', unsafe_allow_html=True)
            
            st.title('Activity Map')
            col1, col2 = st.columns(2)
            with col1:
                st.header("Most busy day")
                busy_day = week_activity_map(selected_user,df)
                fig,ax = plt.subplots(figsize=(8,6))
                ax.bar(busy_day.index,busy_day.values, color='skyblue',alpha=0.8)
                ax.set_xlabel("Day")
                ax.set_ylabel("Messages")
                ax.set_title("Most Busy Day")
                ax.grid(True, linestyle='--', alpha=0.7)
                ax.patch.set_facecolor('whitesmoke')
                ax.patch.set_alpha(0.9)
                plt.xticks(rotation='vertical')
                plt.tight_layout()
                st.pyplot(fig)
            with col2:
                st.header("Most busy Month")
                busy_month = month_activity_map(selected_user,df)
                fig,ax = plt.subplots(figsize=(8,6))
                ax.bar(busy_month.index,busy_month.values,color='orange', alpha=0.8)
                ax.set_xlabel("Month")
                ax.set_ylabel("Messages")
                ax.set_title("Most Busy Month")
                ax.grid(True, linestyle='--', alpha=0.7)
                ax.patch.set_facecolor('whitesmoke')
                ax.patch.set_alpha(0.9)
                plt.xticks(rotation='vertical')
                plt.tight_layout()
                st.pyplot(fig)
            
            st.markdown('<div class="dotted-line"></div>', unsafe_allow_html=True)
            
            st.title("Weekly activity map")
            user_heatmap = activity_heatmap(selected_user,df)
            fig,ax=plt.subplots(figsize=(10,6))
            ax = sns.heatmap(user_heatmap, ax=ax, cmap="YlGnBu", linewidths=0.5, linecolor='white', annot=True)
            ax.set_xlabel("Day of Week")
            ax.set_ylabel("Hour of Day")
            ax.set_title("Weekly Activity Map")    
            plt.tight_layout()    
            st.pyplot(fig)

            st.markdown('<div class="dotted-line"></div>', unsafe_allow_html=True)
            
            if selected_user == 'Overall':
                st.title('Most Busy users')
                x, new_df = most_busy_users(df)
                fig, ax = plt.subplots(figsize=(10, 6))
                bars = ax.bar(x.index, x.values, color='skyblue', alpha=0.8)
                plt.xticks(rotation='vertical')
                ax.set_xlabel("User")
                ax.set_ylabel("Messages")
                ax.set_title("Most Busy Users")
                ax.grid(True, linestyle='--', alpha=0.7)
                ax.patch.set_facecolor('whitesmoke')
                ax.patch.set_alpha(0.9)
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
                st.dataframe(new_df)
                
            st.markdown('<div class="dotted-line"></div>', unsafe_allow_html=True)

            st.title("WordCloud")
            df_wc = create_wordcloud(selected_user, df)
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.imshow(df_wc)
            ax.axis('off')
            ax.set_title("WordCloud")
            plt.tight_layout()
            placeholder_wc = st.empty()
            placeholder_wc.pyplot(fig)

            st.markdown('<div class="dotted-line"></div>', unsafe_allow_html=True)
            # Most common words
            most_common_df = most_common_words(selected_user, df)
            fig, ax = plt.subplots(figsize=(10, 6))
            bars = ax.barh(most_common_df['Word'], most_common_df['Count'],color='skyblue', alpha=0.8)
            plt.xticks(rotation='vertical')
            st.title('Most Common Words')
            ax.set_xlabel("Count")
            ax.set_ylabel("Word")
            ax.set_title("Most Common Words")
            ax.grid(True, linestyle='--', alpha=0.7)
            ax.patch.set_facecolor('whitesmoke')
            ax.patch.set_alpha(0.9)
            plt.tight_layout()
            st.dataframe(most_common_df)
            placeholder_most_common = st.empty()
            placeholder_most_common.pyplot(fig)

            st.markdown('<div class="dotted-line"></div>', unsafe_allow_html=True)
            
            #emoji analysis
            emoji_df = emoji_helper(selected_user,df)
            st.title("Emoji Analysis")

            col1,col2 = st.columns(2)

            with col1:
                st.dataframe(emoji_df)
            with col2:
                fig,ax = plt.subplots(figsize=(8,8))
                ax.pie(emoji_df[1].head(),labels=emoji_df[0].head(),autopct="%0.2f",colors=sns.color_palette("Set3", len(emoji_df[0])))
                ax.set_title("Emoji Distribution")
                plt.tight_layout()
                placeholder_emoji = st.empty()
                placeholder_emoji.pyplot(fig)

            