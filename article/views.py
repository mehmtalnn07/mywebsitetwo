from django.shortcuts import render

def index(request):    
    return render(request,"index.html")

def resume(request):
    return render(request,"resume.html")

def aboutMe(request):
    return render(request, "aboutMe.html")

def mobileProjects(request):
    return render(request, "mobileProjects.html")

def webProjects(request):
    return render(request, "webProjects.html")

def cyberSecurityProjects(request):
    return render(request, "cyberSecurityProjects.html")

def desktopProjects(request):
    return render(request, "desktopProjects.html")

def notFound(request):
    return render(request, "notfound.html")

def contact(request):
    return render(request, "contact.html")

def sourceCode(request):
    return render(request, "sourceCode.html")

def comingSoon(request):
    return render(request, "comingSoon.html")

def notFound(request, exception=None):
    return render(request, "notFound.html", status=404)


def plansImagesViews(request):
    image_paths = [
        '/static/projectsImages/plansImages/plans1.png',
        '/static/projectsImages/plansImages/plans2.png',
        '/static/projectsImages/plansImages/plans3.png',
        '/static/projectsImages/plansImages/plans4.png',
        '/static/projectsImages/plansImages/plans5.png',
        '/static/projectsImages/plansImages/plans6.png',
        '/static/projectsImages/plansImages/plans7.png',
        '/static/projectsImages/plansImages/plans8.png',
    ]
    context = {
        'title': 'Plans',
        'project_title': 'Plans',
        'image_paths': image_paths,
    }
    
    return render(request, 'mobileProjectImages.html', context)


def plansIOSViews(request):
    context = {
        'pageUrl': "plansImages",
        'title': 'Plans',
        'project_name': "- Plans IOS -",
        'project_purpose': "The 'Plans' application is designed to facilitate task management and productivity enhancement for users. It leverages modern technologies and SwiftUI framework to provide a seamless user experience. Let's delve into the details of its structure, functionalities, and design principles.",
        'technologies_used_one': "- Technologies Used -",
        'technologies_used_one_card_one': "- Swift UI:",
        'technologies_used_one_card_one_content': "The entire application is built using SwiftUI, Apple's declarative framework for building user interfaces across all Apple platforms.",
        'technologies_used_one_card_two': "- Firebase:",
        'technologies_used_one_card_two_content': "Firebase Authentication and Firestore are utilized for user authentication and real-time data storage, respectively.",
        'technologies_used_one_card_three': "- MVVM Architecture:",
        'technologies_used_one_card_three_content': "The application follows the Model-View-ViewModel architectural pattern to separate concerns and ensure maintainability and testability.",
        'technologies_used_one_card_four': "- SwiftUI Components:",
        'technologies_used_one_card_four_content': "Various SwiftUI components such as NavigationView, List, Form, Button, TextField, SecureField, and DatePicker are employed to create a responsive and intuitive user interface.",
        'technologies_used_two': "- Design Principles -",
        'technologies_used_two_card_one': "- User-Friendly Interface:",
        'technologies_used_two_card_one_content': "'Emphasis on intuitive UI components such as lists, forms, and buttons to enhance usability.",
        'technologies_used_two_card_two': "- Responsive Design:",
        'technologies_used_two_card_two_content': "Utilization of SwiftUI's layout components to ensure the application adapts seamlessly to different screen sizes.",
        'technologies_used_two_card_three': "- Real-Time Updates:",
        'technologies_used_two_card_three_content': "Leveraging Firestore for real-time data updates to provide users with up-to-date task information.",
        'technologies_used_two_card_four': "- Security:",
        'technologies_used_two_card_four_content': "Authentication and data management handled securely using Firebase services.",
        'conclusion_content': "The 'Plans' application exemplifies efficient task management and productivity enhancement through its use of SwiftUI and Firebase technologies. It provides a robust foundation for users to organize their tasks effectively, register securely, and manage their profiles seamlessly. The MVVM architecture ensures separation of concerns, making the application scalable and maintainable. This project not only showcases modern iOS development techniques but also prioritizes user experience, making it a valuable tool for anyone looking to streamline their task management process."
    }
    return render(request, "projectIntroduction.html", context)

def facetimeImagesViews(request):
    image_paths = [
        '/static/projectsImages/facetimeImages/facetime1.png',
        '/static/projectsImages/facetimeImages/facetime2.png',
        '/static/projectsImages/facetimeImages/facetime3.png',
        '/static/projectsImages/facetimeImages/facetime4.png',
        '/static/projectsImages/facetimeImages/facetime5.png',
        '/static/projectsImages/facetimeImages/facetime6.png',
    ]
    context = {
        'title': 'FaceTime',
        'project_title': 'FaceTime',
        'image_paths': image_paths,
    }
    
    return render(request, 'mobileProjectImages.html', context)


def facetimeViews(request):
    context = {
        'pageUrl': "facetimeImages",
        'title': 'Facetime',
        'project_name': "- Facetime -",
        'project_purpose': "The FaceTime application is an iOS platform that enables users to engage in real-time video calls. It also incorporates authentication functionalities to facilitate user access.",
        'technologies_used_one': "- Technologies and Frameworks Used -",
        'technologies_used_one_introduction': "This interface is designed to capture customer information and store it in an SQLite database. Key features include:",
        'technologies_used_one_card_one': "- Firebase Authentication:",
        'technologies_used_one_card_one_content': "Utilized for user authentication processes, allowing users to securely register, log in, and log out of the application.",
        'technologies_used_one_card_two': "- Stream Video Frameworks:",
        'technologies_used_one_card_two_content': "This includes **StreamVideo** for real-time video streaming, **StreamVideoUIKit** for UI components, and **StreamVideoSwiftUI** for SwiftUI views.",
        'technologies_used_two': "- Architecture and Functionality -",
        'technologies_used_two_card_one': "- CallManager:",
        'technologies_used_two_card_one_content': "'Manages the setup and configuration of the StreamVideo framework for handling video calls, initializing credentials, and establishing connections.",
        'technologies_used_two_card_two': "- AuthManager:",
        'technologies_used_two_card_two_content': "Centralizes user authentication operations using Firebase Authentication, handling sign-in, sign-up, and sign-out functionalities.",
        'technologies_used_two_card_three': "- WelcomeView:",
        'technologies_used_two_card_three_content': "The initial interface for users to sign in or sign up.",
        'technologies_used_two_card_four': "- AccountViewController:",
        'technologies_used_two_card_four_content': "The main interface for authenticated users to initiate and manage video calls.",
        'conclusion_content': "The FaceTime application integrates advanced video streaming capabilities with secure user authentication, creating an engaging platform for real-time communication."
    }
    return render(request, "projectIntroduction.html", context)



def flutterWeatherAppImagesViews(request):
    image_paths = [
        '/static/projectsImages/flutterWeatherAppImages/flutter_weather_app_images1.gif',
        '/static/projectsImages/flutterWeatherAppImages/flutter_weather_app_images2.gif',
        '/static/projectsImages/flutterWeatherAppImages/flutter_weather_app_images3.gif',
        '/static/projectsImages/flutterWeatherAppImages/flutter_weather_app_images4.gif',
    ]
    context = {
        'title': 'Flutter Weather App',
        'project_title': 'Flutter Weather App',
        'image_paths': image_paths,
    }
    
    return render(request, 'mobileProjectImages.html', context)


def flutterWeatherAppViews(request):
    context = {
        'pageUrl': "flutterWeatherAppImages",
        'title': 'FlutterWeatherApp',
        'project_name': "- Flutter Weather App -",
        'project_purpose': "This Flutter project is a mobile application that visually presents weather information based on the user's current location or a selected city. The user interface incorporates Lottie animations to enhance visual appeal, with dynamic background animations reflecting the current weather conditions.",
        'technologies_used_one': "- Technologies Used -",
        'technologies_used_one_card_one': "- Flutter Framework:",
        'technologies_used_one_card_one_content': "Used for building the UI, allowing for natively compiled applications for mobile, web, and desktop from a single codebase.",
        'technologies_used_one_card_two': "- Dart Programming Language:",
        'technologies_used_one_card_two_content': "The primary language for Flutter, offering a modern, efficient, and type-safe language for development.",
        'technologies_used_one_card_three': "- HTTP Package:",
        'technologies_used_one_card_three_content': "Integrated to fetch real-time weather data from the OpenWeatherMap API.",
        'technologies_used_one_card_four': "- Geolocator & Geocoding:",
        'technologies_used_one_card_four_content': "Packages used to determine the user's current location and translate coordinates into a readable city name.",
        'technologies_used_one_card_five': "- Lottie Package:",
        'technologies_used_one_card_five_content': "Used for integrating JSON-based animations to create a dynamic and visually appealing user experience.",
        'technologies_used_two': "- Project Workflow -",
        'technologies_used_two_card_one': "- Initialization:",
        'technologies_used_two_card_one_content': "'The WeatherScreen widget is displayed upon launching the application.",
        'technologies_used_two_card_two': "- Location Permission:",
        'technologies_used_two_card_two_content': "Checks and requests necessary permissions for accessing the user's location.",
        'technologies_used_two_card_three': "- Weather Data Retriveal:",
        'technologies_used_two_card_three_content': "Fetches user coordinates, converts them to a city name, and sends an API request to OpenWeatherMap for weather data.",
        'technologies_used_two_card_four': "- Data Presentation:",
        'technologies_used_two_card_four_content': "The UI is dynamically updated with fetched weather data, including temperature and weather conditions.",
        'technologies_used_two_card_five': "- Visual Representation:",
        'technologies_used_two_card_five_content': "Appropriate Lottie animations are integrated as background and icons based on the current weather condition.",
        'conclusion_content': "This project showcases effective utilization of Flutter's capabilities to create a responsive and visually appealing weather application. By leveraging Dart's efficiency and Flutter's UI flexibility, the application delivers real-time weather updates with a seamless user interface."
    }
    return render(request, "projectIntroduction.html", context)


def notebookImagesViews(request):
    image_paths = [
        '/static/projectsImages/notebookImages/notebook1.jpeg',
        '/static/projectsImages/notebookImages/notebook2.jpeg',
        '/static/projectsImages/notebookImages/notebook3.jpeg',
        '/static/projectsImages/notebookImages/notebook4.jpeg',
        '/static/projectsImages/notebookImages/notebook5.jpeg',
        '/static/projectsImages/notebookImages/notebook6.jpeg',
        '/static/projectsImages/notebookImages/notebook7.jpeg', 
        '/static/projectsImages/notebookImages/notebook8.jpeg',
        '/static/projectsImages/notebookImages/notebook9.jpeg',
        '/static/projectsImages/notebookImages/notebook10.jpeg',
    ]
    context = {
        'title': 'Notebook',
        'project_title': 'Notebook',
        'image_paths': image_paths,
    }
    
    return render(request, 'mobileProjectImages.html', context)


def notebookViews(request):
    context = {
        'pageUrl': "notebookImages",
        'title': 'Notebook',
        'project_name': "- Notebook -",
        'project_purpose': "The Notebook application is an Android project designed to manage notes. The application leverages several modern technologies and follows architectural best practices to ensure robustness, maintainability, and scalability. Below is a detailed analysis of the technologies, architecture, and design patterns used in this project.",
        'technologies_used_one': "- Technologies Used -",
        'technologies_used_one_card_one': "- Programming Language:",
        'technologies_used_one_card_one_content': "Kotlin is the primary programming language used in this project. It is known for its conciseness, safety features, and full interoperability with Java.",
        'technologies_used_one_card_two': "- Android Jetpack Libraries:",
        'card_two_content_title_one': "1 - Room -",
        'card_two_content_title_one_content': "Used for local database management. It provides an abstraction layer over SQLite to allow fluent database access while harnessing the full power of SQLite.",
        'card_two_content_title_two': "2 - ViewModel -",
        'card_two_content_title_two_content': "Used to store and manage UI-related data in a lifecycle-conscious way. This allows data to survive configuration changes such as screen rotations.",
        'card_two_content_title_three': "3 - LiveData -",
        'card_two_content_title_three_content': "Not explicitly seen in the provided snippets but commonly used with ViewModel for observing data changes.",
        'technologies_used_one_card_three': "- Material Design Components:",
        'card_three_content_title_one': "1 - Material3 -",
        'card_three_content_title_one_content': "The application uses Material3 components for UI elements, ensuring a modern and consistent user interface.",
        'card_three_content_title_two': "2 - Compose -",
        'card_three_content_title_two_content': "Jetpack Compose is used for building UI. It simplifies and accelerates UI development on Android with less code and powerful tools.",
        'technologies_used_one_card_four': "- Coroutines:",
        'technologies_used_one_card_four_content': "Kotlin Coroutines are used for asynchronous programming, providing a simple and efficient way to handle background tasks.",
        'technologies_used_two': "- Architectural Patterns -",
        'card_one_content_title_one': "1 - Model -",
        'card_one_content_title_one_content': "Represents the data layer. Includes entities like Note and History, and repositories for data operations.",
        'card_one_content_title_two': "2 - View -",
        'card_one_content_title_two_content': "Composables and UI components that display the data and handle user interactions.",
        'card_one_content_title_three': "3 - ViewModel",
        'card_one_content_title_three_content': "Manages UI-related data and business logic. Examples include HomeViewModel and NoteDetailsViewModel.",
        'technologies_used_two_card_two': "- Repository Pattern:",
        'technologies_used_two_card_two_content': "Abstracts the data sources and provides a clean API for data access to the rest of the application.",
        'technologies_used_two_card_three': "- Singleton Pattern:",
        'technologies_used_two_card_three_content': "Used in database instances (NoteDatabase and HistoryDatabase) to ensure a single instance of the database is created and used throughout the application lifecycle.",
        'conclusion_content': "This project leverages a combination of modern Android technologies and best practices, including Kotlin, Room, Jetpack Compose, and MVVM architecture. The use of Room for database management, coupled with ViewModels for maintaining UI-related data and Jetpack Compose for building the UI, indicates a robust and maintainable structure. Dependency injection is managed manually but effectively within the application class, ensuring clean and testable code. The application's architecture and choice of technologies ensure scalability, maintainability, and a responsive user experience."
    }
    return render(request, "projectIntroduction.html", context)



def wordGuessGameImagesViews(request):
    image_paths = [
        '/static/projectsImages/wordGuessGame/wordGuessGame1.jpeg',
        '/static/projectsImages/wordGuessGame/wordGuessGame2.jpeg',
        '/static/projectsImages/wordGuessGame/wordGuessGame3.jpeg',
        '/static/projectsImages/wordGuessGame/wordGuessGame4.jpeg',
        '/static/projectsImages/wordGuessGame/wordGuessGame5.jpeg',
        '/static/projectsImages/wordGuessGame/wordGuessGame6.jpeg',
        '/static/projectsImages/wordGuessGame/wordGuessGame7.jpeg',
        '/static/projectsImages/wordGuessGame/wordGuessGame8.jpeg',
    ]
    context = {
        'title': 'WordGuessGame',
        'project_title': 'Word Guess Game',
        'image_paths': image_paths,
    }
    
    return render(request, 'mobileProjectImages.html', context)


def wordGuessGameViews(request):
    context = {
        'pageUrl': "wordGuessGameImages",
        'title': 'WordGuessGame',
        'project_name': "- Word Guess Game -",
        'project_purpose': "The project aims to provide users with an interactive word guessing game where they can enhance their vocabulary and compete with others. Users progress through different levels within each category, guessing words to earn points and potentially climb the leaderboard.",
        'technologies_used_one': "- Technologies Used -",
        'technologies_used_one_card_one': "- Firebase:",
        'card_one_content_title_one': "1 - Firebase Authentication -",
        'card_one_content_title_one_content': "Enables user authentication, allowing users to register, log in, and manage their accounts securely.",
        'card_one_content_title_two': "2 - Firebase Realtime Database -",
        'card_one_content_title_two_content': "Utilized for storing dynamic data such as user information, game states, and user scores in real-time.",
        'card_one_content_title_three': "3 - Firebase Cloud Firestore -",
        'card_one_content_title_three_content': "Used to store static data such as word lists for different game levels and categories.",
        'technologies_used_two': "- Architectural Considerations -",
        'technologies_used_two_introduction': "The architecture of the application follows a ViewModel-driven approach using Android's recommended architecture components",
        'technologies_used_two_card_one': "- ViewModel:",
        'technologies_used_two_card_one_content': "Manages UI-related data in a lifecycle-conscious way. In this context, AuthViewModel handles user authentication and registration logic, while GameViewModel manages game state, including word lists, game invitations, and user scores.",
        'technologies_used_two_card_two': "- LiveData & StateFlow:",
        'technologies_used_two_card_two_content': "These are used for reactive programming, enabling the UI to automatically update in response to changes in underlying data.",
        'technologies_used_two_card_three': "- Coroutines:",
        'technologies_used_two_card_three_content': "Leveraged for asynchronous programming, particularly in handling Firebase operations and fetching data from Firestore.",
        'conclusion_content': "The project effectively utilizes Firebase services to create a responsive and interactive word guessing game application. By leveraging ViewModel architecture and Firebase's real-time capabilities, the app delivers a seamless user experience with real-time updates and synchronized data management. This architecture not only enhances user engagement but also ensures efficient data handling and scalability."
    }
    return render(request, "projectIntroduction.html", context)




def twitterImagesViews(request):
    image_paths = [
        '/static/projectsImages/twitterCloneImages/twitter1.jpeg',
        '/static/projectsImages/twitterCloneImages/twitter2.jpeg',
        '/static/projectsImages/twitterCloneImages/twitter3.jpeg',
        '/static/projectsImages/twitterCloneImages/twitter4.jpeg',
        '/static/projectsImages/twitterCloneImages/twitter5.jpeg',
        '/static/projectsImages/twitterCloneImages/twitter6.jpeg',
        '/static/projectsImages/twitterCloneImages/twitter7.jpeg',
        '/static/projectsImages/twitterCloneImages/twitter8.jpeg',
    ]
    context = {
        'title': 'TwitterClone',
        'project_title': 'Twitter Clone',
        'image_paths': image_paths,
    }
    
    return render(request, 'mobileProjectImages.html', context)


def twitterViews(request):
    context = {
        'pageUrl': "twitterImages",
        'title': 'TwitterClone',
        'project_name': "- Twitter Clone -",
        'project_purpose': "The provided code snippets are part of a comprehensive application that resembles a social media platform. This application is designed using modern Android development principles and leverages Firebase for real-time database and authentication functionalities.",
        'technologies_used_one': "- Key Features and Components -",
        'technologies_used_one_card_one': "- Navigation Setup (NavGraph and MyBottomBar):",
        'card_one_content_title_one': "1 - NavGraph -",
        'card_one_content_title_one_content': "Manages navigation throughout the app using Jetpack Compose's NavHost and composable functions for different screens such as login, registration, home feed, notifications, user profile, and others.",
        'card_one_content_title_two': "2 - MyBottomBar -",
        'card_one_content_title_two_content': "Custom bottom navigation bar implemented with Material3 components, facilitating easy navigation between main sections of the app.",
        'technologies_used_one_card_two': "- User Data Management (SharedPreferences):",
        'card_two_content_title_one': "1 - SharedPreferences -",
        'card_two_content_title_one_content': "Manages local storage of user data using Android's SharedPreferences, storing information such as name, surname, username, bio, email, image URL, and phone number. Provides methods to store and retrieve user-specific data across different parts of the application.",
        'technologies_used_one_card_three': "- ViewModelArchitecture (UserViewModel):",
        'card_three_content_title_one': "1 - UserViewModel -",
        'card_three_content_title_one_content': "UserViewModel utilizes Android's ViewModel to handle data logic and lifecycle-aware data propagation to UI components. Implements Firebase's real-time database (FirebaseDatabase) and Firestore (FirebaseFirestore) to fetch and update user profiles, bweets (posts), followers, and followings. Supports functions for fetching user details, fetching bweets, following/unfollowing users, and retrieving follower/following lists.",
        'technologies_used_one_card_four': "- Screens and Navigation:",
        'technologies_used_one_card_four_content': "The application includes various screens like Home, Search, AddBweet, Notification, Profile, OtherUser, FollowersScreen, FollowingsScreen, and more. Each screen is connected through navigation routes defined in a centralized Routes object, ensuring consistent and predictable navigation flow.",
        'technologies_used_two': "- Technologies and Libraries Used -",
        'technologies_used_two_card_one': "- Jetpack Compose:",
        'technologies_used_two_card_one_content': "Modern Android UI toolkit for building native UIs.",
        'technologies_used_two_card_two': "- Firebase:",
        'technologies_used_two_card_two_content': "Backend services including Firebase Realtime Database and Firestore for real-time data synchronization.",
        'technologies_used_two_card_three': "- ViewModel and LiveData:",
        'technologies_used_two_card_three_content': "Architecture components for managing UI-related data in a lifecycle-conscious way.",
        'technologies_used_two_card_four': "- Material3 Components:",
        'technologies_used_two_card_four_content': "Used for consistent and attractive UI design, including icons and navigation components.",
        'technologies_used_two_card_five': "- Kotlin Coroutines:",
        'technologies_used_two_card_five_content': "Asynchronous programming to manage long-running tasks.",
        'conclusion_content': "The described project showcases a modern Android application resembling a social media platform, developed using cutting-edge technologies and architectural principles. By leveraging Jetpack Compose for UI design, Firebase for backend services including real-time database and Firestore, and Kotlin coroutines for asynchronous operations, the app delivers a responsive and interactive user experience. Key features such as navigation management through NavGraph and MyBottomBar, user data handling with SharedPreferences, and robust data management using ViewModel and Firebase's database solutions ensure a seamless flow from user authentication to profile management, post interactions, and social connections. With its focus on scalability, real-time updates, and user-centric design, the project aims to provide a user-friendly interface akin to popular social media platforms while demonstrating best practices in Android development and Firebase integration. This comprehensive approach not only enhances user engagement but also underscores the importance of efficient data handling and responsive UI design in modern mobile applications."
    }
    return render(request, "projectIntroduction.html", context)



def threadsImagesViews(request):
    image_paths = [
        '/static/projectsImages/threadsCloneImages/threads1.jpeg',
        '/static/projectsImages/threadsCloneImages/threads2.jpeg',
        '/static/projectsImages/threadsCloneImages/threads3.jpeg',
        '/static/projectsImages/threadsCloneImages/threads4.jpeg',
        '/static/projectsImages/threadsCloneImages/threads5.jpeg',
        '/static/projectsImages/threadsCloneImages/threads6.jpeg',
        '/static/projectsImages/threadsCloneImages/threads7.jpeg',
    ]
    context = {
        'title': 'ThreadsClone',
        'project_title': 'Threads Clone',
        'image_paths': image_paths,
    }
    
    return render(request, 'mobileProjectImages.html', context)


def threadsCloneViews(request):
    context = {
        'pageUrl': "threadsImages",
        'title': 'ThreadsClone',
        'project_name': "- Threads Clone -",
        'project_purpose': "The Threads Clone project is an Android application designed to replicate the functionality of a modern messaging platform, implemented using contemporary technologies and architectural patterns. The application utilizes Jetpack Compose for its declarative UI framework, Firebase for backend services including real-time database and Firestore, and Kotlin coroutines for efficient asynchronous programming.",
        'technologies_used_one': "- Technology Stack and Architecture -",
        'technologies_used_one_card_one': "- Jetpack Compose:",
        'technologies_used_one_card_one_content': "Used for building the UI components of the application in a declarative manner, ensuring a responsive and dynamic user interface.",
        'technologies_used_one_card_two': "- Firebase Realtime Database and Firestore:",
        'technologies_used_one_card_two_content': "These are employed for managing real-time messaging, user data, and message threads. Realtime updates are crucial for providing users with instant message notifications and seamless communication experiences.",
        'technologies_used_one_card_three': "- Kotlin Coroutines:",
        'technologies_used_one_card_three_content': "Leveraged for managing asynchronous tasks efficiently, such as fetching data from Firebase and updating the UI without blocking the main thread.",
        'technologies_used_one_card_four': "- ViewModel:",
        'technologies_used_one_card_four_content': "Utilized to store and manage UI-related data in a lifecycle-conscious way, ensuring data persistence and proper management across configuration changes.",
        'technologies_used_two': "- Application Structure -",
        'technologies_used_two_introduction': "The architecture of the Threads Clone application is structured to facilitate easy navigation, data management, and user interaction.",
        'technologies_used_two_card_one': "- NavGraph:",
        'technologies_used_two_card_one_content': "Defines the navigation flow within the application, directing users through different screens such as login, messaging threads, user profiles, and settings. Each screen is associated with a specific route defined in the NavGraph.",
        'technologies_used_two_card_two': "- Bottom Navigation:",
        'technologies_used_two_card_two_content': "Similar to the social media app, the Threads Clone app includes a bottom navigation bar allowing users to navigate between key sections like messaging threads, contacts, notifications, and settings. This navigation component enhances user experience by providing quick access to essential features.",
        'technologies_used_two_card_three': "- User Data Management:",
        'technologies_used_two_card_three_content': "Implemented using SharedPreferences for local user data storage, ensuring seamless access to user information such as profile details and session data.",
        'technologies_used_two_card_four': "- Firebase Integration:",
        'technologies_used_two_card_four_content': "Handles user authentication, real-time message synchronization, and data storage. Firebase Firestore manages complex queries and transactions, ensuring that message threads are updated in real-time across devices.",
        'conclusion_content': "The Threads Clone project showcases a robust Android application that mimics the functionality of a modern messaging platform, emphasizing real-time communication and user engagement. By leveraging Jetpack Compose for dynamic UI, Firebase for scalable backend services, and Kotlin coroutines for efficient asynchronous operations, the app provides a seamless and responsive user experience. This project not only demonstrates proficiency in Android development and Firebase integration but also highlights best practices in UI design and data management. The Threads Clone application aims to deliver a user-friendly interface akin to popular messaging platforms while emphasizing scalability, real-time updates, and efficient data handling."
    }
    return render(request, "projectIntroduction.html", context)


def weatherImagesViews(request):
    image_paths = [
        '/static/projectsImages/weatherAppImages/weather1.jpeg',
        '/static/projectsImages/weatherAppImages/weather2.jpeg',
        '/static/projectsImages/weatherAppImages/weather3.jpeg',
        '/static/projectsImages/weatherAppImages/weather4.jpeg',
    ]
    context = {
        'title': 'Weather',
        'project_title': 'Weather',
        'image_paths': image_paths,
    }
    
    return render(request, 'mobileProjectImages.html', context)


def weatherAppViews(request):
    context = {
        'pageUrl': "weatherImages",
        'title': 'Weather',
        'project_name': "- Weather App -",
        'project_purpose': "The weather application project is designed to provide users with up-to-date weather information for various locations. It leverages modern Android development practices to deliver a responsive and intuitive user experience.",
        'technologies_used_one': "- Technologies and Used -",
        'technologies_used_one_introduction': "The application features a sleek bottom navigation bar that allows seamless navigation between different sections.",
        'technologies_used_one_card_one': "- Kotlin:",
        'technologies_used_one_card_one_content': "The preferred programming language for Android development, known for its conciseness and safety features.",
        'technologies_used_one_card_two': "- Android Jetpack Components:",
        'technologies_used_one_card_two_content': "Including ViewModel, LiveData (StateFlow), and Lifecycle components to manage UI-related data in a lifecycle-conscious way.",
        'technologies_used_one_card_three': "- Retrofit:",
        'technologies_used_one_card_three_content': "A type-safe HTTP client for Android and Java, used for making network requests to fetch weather data from a remote API.",
        'technologies_used_one_card_four': "- Coroutines:",
        'technologies_used_one_card_four_content': "Kotlin’s lightweight concurrency framework employed for managing asynchronous programming tasks, ensuring smooth and responsive app performance.",
        'technologies_used_one_card_five': "- Dependency Injection with Koin:",
        'technologies_used_one_card_five_content': "Simplifies the project’s dependency management by providing a lightweight yet powerful DI framework.",
        'technologies_used_two': "- Architecture -",
        'technologies_used_two_introduction': "The project adheres to the MVVM (Model-View-ViewModel) architecture pattern.",
        'technologies_used_two_card_one': "- Model:",
        'technologies_used_two_card_one_content': "Defines the data structures (Location, DailyForecasts, HourlyForecast) used throughout the application.",
        'technologies_used_two_card_two': "- View:",
        'technologies_used_two_card_two_content': "Represents UI components and layouts, responsible for presenting data and interacting with users.",
        'technologies_used_two_card_three': "- ViewModel:",
        'technologies_used_two_card_three_content': "Acts as an intermediary between the View and Model layers, managing UI-related data and handling business logic.",
        'technologies_used_two_card_four': "- Repository:",
        'technologies_used_two_card_four_content': "Abstracts the data sources (in this case, the network API) from the ViewModel, promoting separation of concerns and facilitating unit testing.",
        'conclusion_content': "The weather application project showcases a robust implementation of modern Android development practices. By utilizing Kotlin, Jetpack components, Retrofit with Coroutines, and a structured MVVM architecture, the project ensures high performance, maintainability, and scalability. It effectively separates concerns between UI, business logic, and data access layers, promoting code reusability and testability. This comprehensive setup not only enhances the user experience with real-time weather updates but also provides developers with a solid foundation for building and extending similar applications in the future."
    }
    return render(request, "projectIntroduction.html", context)



def recipeImagesViews(request):
    image_paths = [
        '/static/projectsImages/recipeImages/recipe1.jpeg',
        '/static/projectsImages/recipeImages/recipe2.jpeg',
        '/static/projectsImages/recipeImages/recipe3.jpeg',
        '/static/projectsImages/recipeImages/recipe4.jpeg',
        '/static/projectsImages/recipeImages/recipe5.jpeg',
        '/static/projectsImages/recipeImages/recipe6.jpeg',
        '/static/projectsImages/recipeImages/recipe7.jpeg',
    ]
    context = {
        'title': 'Recipe',
        'project_title': 'Recipe',
        'image_paths': image_paths,
    }
    
    return render(request, 'mobileProjectImages.html', context)



def recipeViews(request):
    context = {
        'pageUrl': "recipeImages",
        'title': 'Recipe',
        'project_name': "- Recipe -",
        'project_purpose': "The recipe application project aims to provide users with a collection of recipes categorized into various food types. It utilizes modern Android development techniques to create a dynamic and engaging user interface.",
        'technologies_used_one': "- Technologies and Tools -",
        'technologies_used_one_card_one': "- Kotlin:",
        'technologies_used_one_card_one_content': "Primary programming language known for its conciseness and safety features.",
        'technologies_used_one_card_two': "- Android Jetpack Compose:",
        'technologies_used_one_card_two_content': "Jetpack’s modern toolkit for building native UIs, facilitating a declarative and reactive programming model.",
        'technologies_used_one_card_three': "- Navigation Component:",
        'technologies_used_one_card_three_content': "Part of Jetpack, simplifying navigation between different screens and passing data between destinations.",
        'technologies_used_one_card_four': "- Material Design 3:",
        'technologies_used_one_card_four_content': "Utilizes Material Design components for a cohesive and visually appealing user interface.",
        'technologies_used_one_card_five': "- Dependency Injection:",
        'technologies_used_one_card_five_content': "Utilizes Compose’s integration with DI frameworks for managing dependencies effectively.",
        'technologies_used_two': "- Architecture -",
        'technologies_used_two_introduction': "The project follows a structured approach to UI development.",
        'technologies_used_two_card_one': "- MVVM Patterns:",
        'used_two_card_one_content_title_one': "1 - Model -",
        'used_two_card_one_content_title_one_content': "Defines data structures (Category, DessertCategory, FoodCategory) representing recipe categories, desserts, and foods.",
        'used_two_card_one_content_title_two': "2 - View -",
        'used_two_card_one_content_title_two_content': "Compose components (HomeScreen, CategoryList, CategoryCard) responsible for displaying UI elements and handling user interactions.",
        'used_two_card_one_content_title_three': "3 - ViewModel",
        'used_two_card_one_content_title_three_content': "Manages UI-related data in a lifecycle-conscious way, facilitating data binding and state management.",
        'technologies_used_two_card_two': "- Jetpack Compose:",
        'technologies_used_two_card_two_content': "Embraces a single-activity architecture with multiple composables for each screen, promoting UI component reusability and modular design.",
        'conclusion_content': "The recipe application project exemplifies modern Android development practices with Jetpack Compose, enhancing UI development with its declarative style and reactive updates. By employing MVVM architecture and leveraging Compose’s capabilities, the project ensures efficient data flow management, UI responsiveness, and code maintainability. This setup not only provides users with an intuitive recipe browsing experience but also equips developers with a scalable foundation for extending the application’s functionality in the future."
    }
    return render(request, "projectIntroduction.html", context)


def voiceRecorderImagesViews(request):
    image_paths = [
        '/static/projectsImages/simpleVoiceRecorderImages/voiceRecorder1.jpeg',
        '/static/projectsImages/simpleVoiceRecorderImages/voiceRecorder2.jpeg',
        '/static/projectsImages/simpleVoiceRecorderImages/voiceRecorder3.jpeg',
        '/static/projectsImages/simpleVoiceRecorderImages/voiceRecorder4.jpeg',
        '/static/projectsImages/simpleVoiceRecorderImages/voiceRecorder5.jpeg',
    ]
    context = {
        'title': 'VoiceRecorder',
        'project_title': 'Voice Recorder',
        'image_paths': image_paths,
    }
    
    return render(request, 'mobileProjectImages.html', context)


def voiceRecorderViews(request):
    context = {
        'pageUrl': "voiceRecorderImages",
        'title': 'VoiceRecorder',
        'project_name': "- Voice Recorder -",
        'project_purpose': "The Voice Recorder application allows users to record, manage, and play audio files directly on their Android devices. It provides an intuitive interface for recording audio, saving files with custom names, and maintaining an organized list of recordings for easy access.",
        'technologies_used_one': "- Technologies and Tools -",
        'technologies_used_one_card_one': "- Kotlin:",
        'technologies_used_one_card_one_content': "The primary programming language used for Android development, offering concise syntax and null safety.",
        'technologies_used_one_card_two': "- Jetpack Compose:",
        'technologies_used_one_card_two_content': "Modern UI toolkit for building declarative, reactive, and maintainable user interfaces.",
        'technologies_used_one_card_three': "- Material Design 3:",
        'technologies_used_one_card_three_content': "Provides a modern, consistent, and visually appealing design system for UI components.",
        'technologies_used_one_card_four': "- MediaRecorder & MediaPlayer API:",
        'technologies_used_one_card_four_content': "Android APIs for recording and playing audio files, enabling core voice recording functionality.",
        'technologies_used_one_card_five': "- Navigation Component:",
        'technologies_used_one_card_five_content': "Handles navigation between different screens such as the recording screen and the recordings list.",
        'technologies_used_two': "- Architecture -",
        'technologies_used_two_introduction': "The application adopts a composable, modular structure to separate UI, logic, and data handling.",
        'technologies_used_two_card_one': "- Jetpack Compose Screens:",
        'technologies_used_two_card_one_content': "Two main composable screens: AudioRecorderApp for recording audio and VoiceList for managing saved recordings.",
        'technologies_used_two_card_two': "- Navigation Graph:",
        'technologies_used_two_card_two_content': "Defines routes for seamless navigation between the recording and listing views.",
        'technologies_used_two_card_three': "- AudioRecorder Class:",
        'technologies_used_two_card_three_content': "Handles starting, stopping, and playing audio using Android's MediaRecorder and MediaPlayer APIs.",
        'technologies_used_two_card_four': "- State Management:",
        'technologies_used_two_card_four_content': "Uses mutableStateOf and remember in Compose for managing recording states, file lists, and dialog visibility.",
        'conclusion_content': "The Voice Recorder project delivers a user-friendly and efficient solution for recording and managing audio files on Android. By leveraging Jetpack Compose, Material Design 3, and Android’s Media APIs, the application offers a modern, responsive interface with smooth navigation and reliable audio handling. Its clean architecture and modular components make it easy to extend, whether for adding cloud backup features, advanced audio editing tools, or enhanced playback options in future versions."
    }
    return render(request, "projectIntroduction.html", context)



def walletImagesViews(request):
    image_paths = [
        '/static/projectsImages/walletImages/wallet1.jpeg',
        '/static/projectsImages/walletImages/wallet2.jpeg',
        '/static/projectsImages/walletImages/wallet3.jpeg',
        '/static/projectsImages/walletImages/wallet4.jpeg',
        '/static/projectsImages/walletImages/wallet5.jpeg',
    ]
    context = {
        'title': 'WalletUI',
        'project_title': 'Wallet UI',
        'image_paths': image_paths,
    }
    
    return render(request, 'mobileProjectImages.html', context)


def walletUiViews(request):
    context = {
        'pageUrl': "walletImages",
        'title': 'WalletUI',
        'project_name': "- Wallet UI -",
        'project_purpose': "The finance application is designed to provide users with a comprehensive view of their financial data through various sections: Bottom Navigation, Card Details, Financial Analytics, and Wallet Overview.",
        'technologies_used_one': "- Bottom Navigation Bar -",
        'technologies_used_one_introduction': "The application features a sleek bottom navigation bar that allows seamless navigation between different sections.",
        'technologies_used_one_card_one': "- Home:",
        'technologies_used_one_card_one_content': "Provides an overview of the user’s financial status and transactions.",
        'technologies_used_one_card_two': "- Wallet:",
        'technologies_used_one_card_two_content': "Displays detailed information about various payment cards, including type, number, current balance, and personalized icons.",
        'technologies_used_one_card_three': "- Notifications:",
        'technologies_used_one_card_three_content': "Alerts users to important updates related to their financial activities.",
        'technologies_used_one_card_four': "- Account:",
        'technologies_used_one_card_four_content': "Provides access to user profile settings and personal information.",
        'technologies_used_two': "- Card Section -",
        'technologies_used_two_introduction': "The Card Section showcases a list of payment cards associated with the user’s account: Each card entry includes essential details such as card type (e.g., VISA, MasterCard), card number (masked for security), card name (e.g., Business, Investment), current balance, and color-coded representation. Users can interact with individual cards, viewing details and initiating actions like transactions or account management.",
        'technologies_used_three': "- Finance Analytics -",
        'technologies_used_three_introduction': "The Finance Analytics section offers insightful data visualization tools: Key financial metrics and performance indicators are displayed through interactive charts and graphs. Users can track their financial health, monitor trends, and make informed decisions based on visualized data.",
        'technologies_used_four': "- User Experience and Design -",
        'technologies_used_four_card_one': "- Modern Design:",
        'technologies_used_four_card_one_content': "The application adheres to Material Design principles, featuring a clean and minimalist interface with intuitive navigation and interactive elements.",
        'technologies_used_four_card_two': "- Responsice Layout:",
        'technologies_used_four_card_two_content': "Designed for optimal viewing across various screen sizes and orientations, ensuring a seamless user experience on mobile devices.",
        'technologies_used_four_card_three': "- Customization:",
        'technologies_used_four_card_three_content': "Users can personalize their experience with customizable settings, preferences, and theme options.",
        'technologies_used_five': "- Development Stack -",
        'technologies_used_five_card_one': "- Jetpack Compose:",
        'technologies_used_five_card_one_content': "Leveraging the latest in Android UI toolkit for declarative UI design and seamless state management.",
        'technologies_used_five_card_two': "- Kotlin:",
        'technologies_used_five_card_two_content': "Utilizing Kotlin for its concise syntax, null safety, and interoperability with existing Java codebase.",
        'technologies_used_five_card_three': "- Android Architecture Components:",
        'technologies_used_five_card_three_content': "Implementing best practices for scalable and maintainable application architecture.",
        'conclusion_content': "The finance application aims to empower users with comprehensive financial insights and tools, facilitating better financial management and decision-making. It combines user-friendly design with robust functionality to deliver a superior mobile banking experience. This project showcases a user-centric approach to financial app development, emphasizing usability, functionality, and aesthetic appeal."
    }
    return render(request, "projectIntroduction.html", context)



def rickAndMortyImagesViews(request):
    image_paths = [
        '/static/projectsImages/reactRickAndMortyImages/rickAndMorty1.png',
        '/static/projectsImages/reactRickAndMortyImages/rickAndMorty2.png',
        '/static/projectsImages/reactRickAndMortyImages/rickAndMorty3.png',
        '/static/projectsImages/reactRickAndMortyImages/rickAndMorty4.png',
    ]
    context = {
        'title': 'RickAndMorty',
        'project_title': 'Rick ANd Morty',
        'image_paths': image_paths,
    }
    
    return render(request, 'mobileProjectImages.html', context)


def rikcAndMortyViews(request):
    context = {
        'pageUrl': "rickAndMortyImages",
        'title': 'RickAndMorty',
        'project_name': "- Rick And Morty -",
        'project_purpose': "This React Native application utilizes the Rick and Morty API to provide information about episodes and characters. Let’s break down its key components.",
        'technologies_used_one': "- Components and Screens -",
        'technologies_used_one_card_one': "- HomeScreen:",
        'technologies_used_one_card_one_content': "",
        'card_one_content_title_one': "1 - Functionality -",
        'card_one_content_title_one_content': "Fetches a list of episodes from 'https://rickandmortyapi.com/api/episode' using fetch and displays them in a FlatList.",
        'card_one_content_title_two': "2 - Navigation -",
        'card_one_content_title_two_content': "Allows users to navigate to DetailsScreen to view more details about each episode.",
        'card_one_content_title_three': "3 - UI -",
        'card_one_content_title_three_content': "Each episode is represented as a Pressable card showing its name, season, and air date.",
        'technologies_used_one_card_two': "- DetailsScreen:",
        'card_two_content_title_one': "1 - Functionality -",
        'card_two_content_title_one_content': "Displays detailed information about a selected episode, including its name, season, air date, and a list of characters.",
        'card_two_content_title_two': "2 - State Management -",
        'card_two_content_title_two_content': "Manages state with useState for episode, characters, loading, and favorites.",
        'card_two_content_title_three': "3 - API Interaction -",
        'card_two_content_title_three_content': "Fetches episode details from 'https://rickandmortyapi.com/api/episode/${id}' and character details from individual character URLs.",
        'card_two_content_title_four': "4 - User Interaction -",
        'card_two_content_title_four_content': "Allows users to add characters to their favorites list with confirmation alerts.",
        'technologies_used_one_card_three': "- Material Design Components:",
        'card_three_content_title_one': "1 - Material3 -",
        'card_three_content_title_one_content': "The application uses Material3 components for UI elements, ensuring a modern and consistent user interface.",
        'card_three_content_title_two': "2 - Compose -",
        'card_three_content_title_two_content': "Jetpack Compose is used for building UI. It simplifies and accelerates UI development on Android with less code and powerful tools.",
        'technologies_used_one_card_four': "- Coroutines:",
        'technologies_used_one_card_four_content': "Kotlin Coroutines are used for asynchronous programming, providing a simple and efficient way to handle background tasks.",
        'technologies_used_two': "- Navigation -",
        'technologies_used_two_card_one': "- React Navigation:",
        'technologies_used_two_card_one_content': "Utilizes NavigationContainer and createStackNavigator to manage navigation between HomeScreen and DetailsScreen.",
        'technologies_used_two_card_two': "- Stack.Navigator:",
        'technologies_used_two_card_two_content': "Configures the stack navigator with options for header visibility and screen titles.",
        'conclusion_content': "This application provides a seamless user experience for exploring Rick and Morty episodes and characters: Users start on the HomeScreen, where they can browse episodes and navigate to detailed information on the DetailsScreen. The DetailsScreen provides extensive episode details and allows users to manage a list of favorite characters. React Native’s components and navigation capabilities ensure a responsive and intuitive mobile app experience."
    }
    return render(request, "projectIntroduction.html", context)




def qrScannerImagesViews(request):
    image_paths = [
        '/static/projectsImages/qrImages/qrScannerImage1.jpeg',
        '/static/projectsImages/qrImages/qrScannerImage2.jpeg',
        '/static/projectsImages/qrImages/qrScannerImage3.jpeg',
        '/static/projectsImages/qrImages/qrScannerImage4.jpeg',
        '/static/projectsImages/qrImages/qrScannerImage5.jpeg',
        '/static/projectsImages/qrImages/qrScannerImage6.jpeg',
        '/static/projectsImages/qrImages/qrScannerImage7.jpeg',
        '/static/projectsImages/qrImages/qrScannerImage8.jpeg',
    ]
    context = {
        'title': 'QR Scanner',
        'project_title': 'QR Scanner',
        'image_paths': image_paths,
    }
    
    return render(request, 'mobileProjectImages.html', context)


def qrCodeScannerViews(request):
    context = {
        'pageUrl': "qrScannerImages",
        'title': 'QRCodeScanner',
        'project_name': "- QR Code Scanner -",
        'project_purpose': "The QR Code Scanner project is a mobile application built using Flutter, designed to facilitate both the generation and scanning of QR codes. This project showcases the versatility of Flutter by integrating multiple functionalities such as user input handling, QR code generation, and barcode scanning.",
        'technologies_used_one': "- Features -",
        'technologies_used_one_card_one': "- HomeScreen:",
        'technologies_used_one_card_one_content': "The Home Screen serves as the central hub of the application, providing users with the option to navigate to either the QR code generation screen or the QR code scanning screen. It includes: A user-friendly interface with two primary buttons for navigation. Integration with Flutter’s Navigator for seamless screen transitions.",
        'technologies_used_one_card_two': "- Generate QR Code Screen:",
        'technologies_used_one_card_two_content': "The Generate QR Code Screen allows users to input text data and generate a corresponding QR code. The generated QR code is displayed on the screen for easy access and use. Key features include: A text input field for user data. Real-time QR code generation using the qr_flutter package. A button to trigger the QR code generation process.",
        'technologies_used_one_card_three': "- Scan QR Code Screen:",
        'technologies_used_one_card_three_content': "The Scan QR Code Screen enables users to scan QR codes and handle the scanned data. It uses the flutter_barcode_scanner package to read QR codes and process the data. Key features include: A button to initiate the QR code scanning process. Real-time scanning and processing of QR codes. Display of the scanned data on the screen. Handling of URLs within QR codes, including validation and launching.",
        'technologies_used_two': "- User Experience -",
        'technologies_used_two_introduction': "The QR Code Scanner project is designed with user experience in mind. It offers a clean and intuitive interface, making it easy for users to generate and scan QR codes. The integration of real-time processing ensures a seamless and efficient user experience. The QR Code Scanner project exemplifies the capabilities of Flutter in building functional and interactive mobile applications. It demonstrates effective use of third-party packages and provides a solid foundation for further enhancements and feature additions.",
        'conclusion_content': "The QR Code Scanner project is a comprehensive mobile application developed using Flutter, designed to provide seamless QR code generation and scanning capabilities. The application includes three main screens: a Home Screen, a Generate QR Code Screen, and a Scan QR Code Screen, each serving distinct purposes to enhance user interaction and functionality.The Home Screen acts as the central navigation hub, offering clear options for generating or scanning QR codes. The Generate QR Code Screen allows users to input text data, which is then converted into a QR code using the qr_flutter package. The Scan QR Code Screen utilizes the flutter_barcode_scanner package to read and process QR codes, with additional handling for URLs to ensure proper validation and launching via the url_launcher package.This project showcases the power of Flutter in building cross-platform mobile applications with efficient and interactive user interfaces. It emphasizes modular design, ensuring maintainability and ease of further development. The integration of real-time data processing and user-friendly navigation enhances the overall user experience, making it a practical tool for various QR code-related tasks."
    }
    return render(request, "projectIntroduction.html", context)

def crmImagesViews(request):
    image_paths = [
        '/static/projectsImages/crmImages/crm1.jpg',
        '/static/projectsImages/crmImages/crm2.jpg',
        '/static/projectsImages/crmImages/crm3.jpg',
        '/static/projectsImages/crmImages/crm4.jpg',
        '/static/projectsImages/crmImages/crm5.jpg',
        '/static/projectsImages/crmImages/crm6.jpg',
        '/static/projectsImages/crmImages/crm7.jpg',
        '/static/projectsImages/crmImages/crm8.jpg',
        '/static/projectsImages/crmImages/crm9.jpg',
        '/static/projectsImages/crmImages/crm10.jpg',
    ]
    context = {
        'title': 'CRM WEB Application',
        'image_paths': image_paths
    }
    return render(request, 'projectsImages.html', context)


def crmWebView(request):
    context = {
        'pageUrl': "crmWebImages",
        'title': 'crmWebImages',
        'project_name': "- CRM WEB Application -",
        'project_purpose': "The aim of this application is to manage customer relationships, collect and analyze customer data, optimize sales processes, and enhance customer satisfaction. Additionally, it helps businesses improve their communication with customers and manage sales opportunities more effectively.",
        'technologies_used_one': "- Technologies Used -",
        'technologies_used_one_card_one': "- HTML:",
        'technologies_used_one_card_one_content': "Used to structure the user interface. Forms, tables, buttons, and other interaction elements were designed using HTML.",
        'technologies_used_one_card_two': "- CSS:",
        'technologies_used_one_card_two_content': "Applied to style HTML elements and make the user interface aesthetically pleasing. Responsive design and various animations were developed using CSS.",
        'technologies_used_one_card_three': "- JavaScript:",
        'technologies_used_one_card_three_content': "Utilized to make user interactions dynamic and manage on-page processes. AJAX calls were used to update data without refreshing the page.",
        'technologies_used_one_card_four': "- Python & Django:",
        'technologies_used_one_card_four_content': "Used to create the backend of the application. Django was chosen for database management, user authentication, data processing, and overall application logic management.",
        'technologies_used_one_card_five': "- Django Admin:",
        'technologies_used_one_card_five_content': "Employed to simplify data management and allow administrators to easily manage user data, sales data, and customer interactions.",
        'technologies_used_two': "- Project Functionality -",
        'technologies_used_two_card_one': "- User Login:",
        'technologies_used_two_card_one_content': "Users can log into the system with a username and password. User authentication is handled by Django's built-in authentication system.",
        'technologies_used_two_card_two': "- Customer Management:",
        'technologies_used_two_card_two_content': "Users can add, update, and delete customer information. Data such as customer notes, contact information, and sales history is stored in the system.",
        'technologies_used_two_card_three': "- Sales Management:",
        'technologies_used_two_card_three_content': "Sales representatives can manage customer relationships and sales opportunities. Sales processes can be tracked and reported.",
        'technologies_used_two_card_four': "- Data Analysis:",
        'technologies_used_two_card_four_content': "The application offers various reporting and analysis tools to analyze customer behavior and sales trends. These tools are powered by Django's data processing capabilities.",
        'technologies_used_two_card_five': "- Django Admin Panel:",
        'technologies_used_two_card_five_content': "Administrators can easily manage all data in the system. This panel simplifies tasks like user management, customer data, and sales data management.",
        'technologies_used_three': "- Key Features -",
        'technologies_used_three_card_one': "- Responsive Design:",
        'technologies_used_three_card_one_content': "The application is designed to work seamlessly on any device, including mobile phones and tablets, providing an optimal viewing experience.",
        'technologies_used_three_card_two': "- User-Firendly Interface:",
        'technologies_used_three_card_two_content': "An easy-to-use and intuitive interface ensures a smooth and efficient user experience.",
        'technologies_used_three_card_three': "- Robust Security:",
        'technologies_used_three_card_three_content': "User data and customer information are protected with strong security measures, leveraging Django's built-in security features for enhanced safety.",
        'technologies_used_three_card_four': "- High Performance:",
        'technologies_used_three_card_four_content': "Data updates are provided without page refreshes using JavaScript and AJAX, significantly enhancing the user experience and application responsiveness.",
        'conclusion_content': "This CRM application helps small and medium-sized businesses manage customer relationships more effectively. Its user-friendly interface, robust backend infrastructure, and flexible data management systems ensure that businesses achieve their goals of increasing sales and customer satisfaction."
    }
    return render(request, "projectIntroduction.html", context)



def sentinelImagesViews(request):
    image_paths = [
        '/static/projectsImages/mitmFoundImages/mitmfound1.jpg',
        '/static/projectsImages/mitmFoundImages/mitmfound2.jpg',
        '/static/projectsImages/mitmFoundImages/mitmfound3.jpg',
        '/static/projectsImages/mitmFoundImages/mitmfound4.jpg',
        '/static/projectsImages/mitmFoundImages/mitmfound5.jpg',
        '/static/projectsImages/mitmFoundImages/mitmfound6.jpg',
    ]
    context = {
        'title': 'MITM Attack Detection Tool',
        'image_paths': image_paths
    }
    return render(request, 'projectsImages.html', context)


def sentinelViews(request):
    context = {
        'pageUrl': "sentinelImages",
        'title': 'Sentinel',
        'project_name': "- Sentinel (MITM Attack Detection Tool) -",
        'project_purpose': "'Sentinel' is a MITM (Man-in-the-Middle) attack detection tool designed to enhance network security. The primary goal of this project is to detect ARP spoofing attacks within a network and alert the user to potential security threats. ARP spoofing is a common form of MITM attack where an attacker intercepts and manipulates communication between devices on a network. 'Sentinel' aims to identify such attacks early, thereby improving the overall security of the network.",
        'technologies_used_one': "- Operationg Environment -",
        'technologies_used_one_introduction': "'Sentinel' is designed to run on Linux operating systems. It is a terminal-based tool developed using Python, which continuously monitors the network’s ARP table. The tool can be utilized in both personal and enterprise networks, offering a simple yet effective way to monitor and secure network traffic.",
        'technologies_used_two': "- How It Works -",
        'technologies_used_two_card_one': "- Monitoring ARP Tables:",
        'technologies_used_two_card_one_content': "'Sentinel' retrieves the ARP table using commands like ip neight or arp-a. The ARP table maps IP addresses to MAC addresses, showing the relationship between devices on the network.",
        'technologies_used_two_card_two': "- Identifying the Gateway MAC Address:",
        'technologies_used_two_card_two_content': "From the ARP table, the tool identifies the device whose IP address ends in '1' (typically the network gateway) and extracts its MAC address. This MAC address belongs to the device that routes traffic within the network.",
        'technologies_used_two_card_three': "- MAC Address Comparison:",
        'technologies_used_two_card_three_content': "The tool compares the gateway's MAC address with the MAC addresses of other devices on the network. If a match is found (i.e., another device shares the same MAC address as the gateway), this may indicate a MITM attack.",
        'technologies_used_two_card_four': "- Alert System:",
        'technologies_used_two_card_four_content': "Upon detecting a potential MITM attack, 'Sentinel' issues an alert to the user via the terminal, enabling immediate action to mitigate the threat.",
        'technologies_used_two_card_five': "- Continuous Monitoring:",
        'technologies_used_two_card_five_content': "The tool operates in a loop, checking the ARP table at regular intervals (every 30 seconds in this case). This ensures continuous monitoring and timely detection of suspicious activity. The interval can be adjusted as needed.",
        'technologies_used_three': "- Technologies Used -",
        'technologies_used_three_card_one': "- Python:",
        'technologies_used_three_card_one_content': "Chosen for its simplicity and readability, allowing for rapid development. Its extensive library support also facilitates easy management of system operations.",
        'technologies_used_three_card_two': "- Linux Command Line (Shell):",
        'technologies_used_three_card_two_content': "The Linux environment allows for direct interaction with system commands via Python using the os.popen() method. This enables seamless execution of network commands.",
        'technologies_used_three_card_three': "- ARP (Address Resolution Protocol):",
        'technologies_used_three_card_three_content': "Essential for mapping IP addresses to MAC addresses. This project leverages ARP to verify the identity of devices on the network.",
        'technologies_used_three_card_four': "- ARP Spoofing/MITM Detection:",
        'technologies_used_three_card_four_content': "MITM attacks pose a significant threat to network security. This project aims to preemptively detect such attacks by identifying ARP spoofing activities.",
        'technologies_used_three_card_five': "- Infinite Loop and Timing:",
        'technologies_used_three_card_five_content': "Continuous network monitoring is crucial, so Python's time.sleep() function is employed for timing. This ensures that potential attacks are detected promptly.",
        'technologies_used_four': "- Usage Instructions -",
        'technologies_used_four_introduction': "To use 'Sentinel', follow these setps:",
        'technologies_used_four_card_one': "- Clone teh Repository:",
        'technologies_used_four_card_one_content': "git clone <repository-url>",
        'technologies_used_four_card_two': "- Navigate to the project directory:",
        'technologies_used_four_card_two_content': "cd <project-directory>",
        'technologies_used_four_card_three': "- Install dependencies (if any):",
        'technologies_used_four_card_three_content': "pip install -r requirements.txt",
        'technologies_used_four_card_four_content': "- Run the tool:",
        'technologies_used_four_card_four_content': "python sentinel.py",
        'conclusion_content': "Monitor the terminal for alerts and take appropriate actions based on the notifications."
    }
    return render(request, "projectIntroduction.html", context)



def macChangerImagesViews(request):
    image_paths = [
        '/static/projectsImages/macchangerImages/macchanger1.jpg',
        '/static/projectsImages/macchangerImages/macchanger2.jpg',
        '/static/projectsImages/macchangerImages/macchanger3.jpg',
        '/static/projectsImages/macchangerImages/macchanger4.jpg',
    ]
    context = {
        'title': 'MAC Changer With Python',
        'image_paths': image_paths
    }
    return render(request, 'projectsImages.html', context)



def macChangerView(request):
    context = {
        'pageUrl': "macChangerImages",
        'title': 'MACChanger',
        'project_name': "- MAC Address Changer -",
        'project_purpose': "This project is a Python-based utility designed to change the MAC address of a network interface on a system. The script is useful for scenarios where you need to spoof or randomize a MAC address, often for security or privacy purposes, such as avoiding network tracking or bypassing MAC address filtering.",
        'technologies_used_one': "- Technologies Used -",
        'technologies_used_one_card_one': "- Python:",
        'technologies_used_one_card_one_content': "The main programming language used for this utility.",
        'technologies_used_one_card_two': "- Subprocess:",
        'technologies_used_one_card_two_content': "This module executes shell commands to interact with the operating system.",
        'technologies_used_one_card_three': "- Argparse:",
        'technologies_used_one_card_three_content': "Used for parsing command-line arguments, allowing user input.",
        'technologies_used_one_card_four': "- RE (Regular Expressions):",
        'technologies_used_one_card_four_content': "Utilized for pattern matching to extract and verify the MAC address.",
        'technologies_used_two': "- Project Functionality -",
        'technologies_used_two_card_one': "- Argument Parsing:",
        'technologies_used_two_card_one_content': "Accepts user inputs for the network interface and new MAC address via command-line arguments.",
        'technologies_used_two_card_two': "- Customer Management:",
        'technologies_used_two_card_two_content': "Users can add, update, and delete customer information. Data such as customer notes, contact information, and sales history is stored in the system.",
        'technologies_used_two_card_three': "- Executing Commands:",
        'technologies_used_two_card_three_content': "Runs shell commands to change the MAC address by bringing the network interface down, modifying the MAC address, and bringing it back up.",
        'technologies_used_two_card_four': "- Verification:",
        'technologies_used_two_card_four_content': "Checks if the MAC address was successfully changed and provides feedback to the user.",
        'technologies_used_three': "- Execution Environment -",
        'technologies_used_three_card_one': "- Operating System:",
        'technologies_used_three_card_one_content': "The script is designed to run on Unix-like operating systems (e.g., Linux, macOS) where the ifconfig command is available. It may require administrative or root privileges to execute correctly.",
        'technologies_used_three_card_two': "- Terminal/Command Line:",
        'technologies_used_three_card_two_content': "The script is executed from a terminal or command-line interface, where the user can pass the required arguments.",
        'conclusion_content': "This project demonstrates how to interact with a system’s network settings using Python. It combines command-line tools with Python scripting to create a utility that is both powerful and flexible, making it suitable for network administrators, security professionals, or anyone needing to modify MAC addresses for testing or privacy reasons."
    }
    return render(request, "projectIntroduction.html", context)


def networkScannerImagesViews(request):
    image_paths = [
        '/static/projectsImages/networkScannerImages/networkScanner1.jpg',
        '/static/projectsImages/networkScannerImages/networkScanner2.jpg',
        '/static/projectsImages/networkScannerImages/networkScanner3.jpg',
    ]
    context = {
        'title': 'Network Scanner With Python',
        'image_paths': image_paths
    }
    return render(request, 'projectsImages.html', context)


def networkScannerView(request):
    context = {
        'pageUrl': "networkScannerImages",
        'title': 'NetworkScanner',
        'project_name': "- Network Scanner -",
        'project_purpose': "The Network Scanner project is designed to scan a network and identify all active devices connected to it. The primary goal of this project is to create a simple and efficient tool for network analysis by utilizing Python. This scanner allows users to identify IP addresses and other network-related details of devices on the same network, providing essential insights for network administrators and security professionals.",
        'technologies_used_one': "- Technologies and Libraries Used -",
        'technologies_used_one_card_one': "- Scapy:",
        'technologies_used_one_card_one_content': "Scapy is a powerful Python library used for network packet manipulation. It provides functionalities for creating, sending, and receiving network packets, making it a suitable choice for tasks like network scanning, packet sniffing, and network analysis. In this project, Scapy is utilized to craft ARP (Address Resolution Protocol) requests, send them over the network, and collect responses from active devices.",
        'technologies_used_one_card_two': "- Optparse:",
        'technologies_used_one_card_two_content': "Optparse is a Python library for parsing command-line options and arguments. It is used here to handle user inputs, specifically to receive the IP address or IP range that the user wants to scan. Although argparse is more commonly used in modern Python projects, optparse is still effective for basic command-line argument handling.",
        'technologies_used_two': "- Architecture and Functionality -",
        'technologies_used_two_card_one': "- Command-Line Input:",
        'technologies_used_two_card_one_content': "The script starts by prompting the user to enter an IP address or a range of IP addresses via the command line. This is handled by the get_input method, which uses optparse to parse the input.",
        'technologies_used_two_card_two': "- Network Scanning:",
        'technologies_used_two_card_two_content': "Once the IP address is provided, the network_scan method is invoked to perform the actual scanning. This method leverages Scapy to create an ARP request targeted at the specified IP address(es). An Ethernet frame is crafted with a broadcast destination, meaning the ARP request is sent to all devices on the local network.",
        'technologies_used_two_card_three': "- ARP Request and Response:",
        'technologies_used_two_card_three_content': "The ARP request is broadcasted over the network, and any active device that receives this request will respond with its MAC address. Scapy’s srp function is used to send the request packet and capture any responses (or the lack thereof).",
        'technologies_used_two_card_four': "- Result Summary:",
        'technologies_used_two_card_four_content': "The script then summarizes the responses, listing out the active devices detected on the network, along with their corresponding IP and MAC addresses. This output is crucial for understanding the devices connected to the network, which can be used for monitoring, security audits, or troubleshooting.",
        'technologies_used_three': "- Practical Applications -",
        'technologies_used_three_card_one': "- Network Administration:",
        'technologies_used_three_card_one_content': "Helps administrators keep track of all devices connected to their network.",
        'technologies_used_three_card_two': "- Security Audits:",
        'technologies_used_three_card_two_content': "Useful for detecting unauthorized devices that may be connected to a network.",
        'technologies_used_three_card_three': "- Troubleshooting:",
        'technologies_used_three_card_three_content': "Assists in identifying network issues by showing which devices are actively communicating.",
        'conclusion_content': "The Network Scanner project is a foundational tool for anyone looking to perform network analysis, providing clear visibility into the devices on a local network and ensuring that network administrators and security experts have the information they need to maintain a secure and efficient network environment."
    }
    return render(request, "projectIntroduction.html", context)



def crmDesktopImagesViews(request):
    image_paths = [
        '/static/projectsImages/crmDesktopImages/crmDesktop1.jpg',
        '/static/projectsImages/crmDesktopImages/crmDesktop2.jpg',
        '/static/projectsImages/crmDesktopImages/crmDesktop3.png',
        '/static/projectsImages/crmDesktopImages/crmDesktop4.png',
        '/static/projectsImages/crmDesktopImages/crmDesktop5.png',
        '/static/projectsImages/crmDesktopImages/crmDesktop6.png',
    ]
    context = {
        'title': 'CRM App With PyQt5',
        'image_paths': image_paths
    }
    return render(request, 'projectsImages.html', context)


def crmDesktopView(request):
    context = {
        'pageUrl' :"crmDesktopImages",
        'title': 'CustomerRelationshipManagement',
        'project_name': "- Customer Relationship Management -",
        'project_purpose': "The project is a comprehensive customer management and user administration system built using Python's PyQt5 library for the user interface and SQLite3 for the database. It allows administrators to manage customers' information, create user accounts, and control user access levels. The system",
        'technologies_used_one': "- Add Customer Interface -",
        'technologies_used_one_introduction': "This interface is designed to capture customer information and store it in an SQLite database. Key features include:",
        'technologies_used_one_card_one': "- İnput Fields:",
        'technologies_used_one_card_one_content': "The form includes fields for first name, last name, email, company name, arrival time, phone number, and a note. These fields are validated to ensure that the data entered ",
        'technologies_used_one_card_two': "- UI Design:",
        'technologies_used_one_card_two_content': "The interface is styled with a modern look, featuring a centered layout, and a color scheme that ensures readability and aesthetic appeal.",
        'technologies_used_one_card_three': "- Database Interaction:",
        'technologies_used_one_card_three_content': "When the 'Save' button is clicked, customer information is validated and saved into an SQLite database. A success message is displayed upon successful entry, and the form fields are cleared for the next input.",
        'technologies_used_two': "- Admin Dashboard -",
        'technologies_used_two_introduction': "The Admin Dashboard provides an overview and management tools for system administrators. Key functionalities include:",
        'technologies_used_two_card_one': "- Welcome Message:",
        'technologies_used_two_card_one_content': "Displays a personalized welcome message to the logged-in admin user.",
        'technologies_used_two_card_two': "- User Management Buttons:",
        'technologies_used_two_card_two_content': "The dashboard includes buttons for creating new users and viewing existing users.",
        'technologies_used_two_card_three': "- Logout Functionality:",
        'technologies_used_two_card_three_content': "An easily accessible logout button allows the admin to exit the dashboard and return to the login screen.",
        'technologies_used_two_card_four': "- Full-Screen Mode:",
        'technologies_used_two_card_four_content': "The dashboard is displayed in full-screen mode, enhancing user focus and ease of use.",
        'technologies_used_three': "- User Creation Interface -",
        'technologies_used_three_introduction': "The User Creation Interface enables admins to add new users to the system. Key features include:",
        'technologies_used_three_card_one': "- Input Fields:",
        'technologies_used_three_card_one_content': "It includes fields for username, password, and an option to assign admin privileges.",
        'technologies_used_three_card_two': "- Validation and Error Handling:",
        'technologies_used_three_card_two_content': "The system checks if the username is already in use and displays an error message if necessary.",
        'technologies_used_three_card_three': "- User Role Assignment:",
        'technologies_used_three_card_three_content': "Admins can assign different roles, such as granting admin rights to new users.",
        'technologies_used_three_card_four': "- Database Interaction:",
        'technologies_used_three_card_four_content': "New user data is securely saved to the SQLite database, and a success message is shown upon successful user creation.",
        'technologies_used_four': "- User Login Interface -",
        'technologies_used_four_introduction': "The User Login Interface is the entry point for all users. It provides:",
        'technologies_used_four_card_one': "- Login Form:",
        'technologies_used_four_card_one_content': "Users input their username and password to gain access.",
        'technologies_used_four_card_two': "- Styling and Layout:",
        'technologies_used_four_card_two_content': "The interface follows a consistent design language with the rest of the application, focusing on simplicity and ease of use.",
        'technologies_used_four_card_three': "- Database Authentication:",
        'technologies_used_four_card_three_content': "Credentials are verified against the stored data in the SQLite database, and upon successful login, the user is redirected to the appropriate dashboard based on their role.",
        'technologies_used_five': "- Technical Details -",
        'technologies_used_five_card_one': "- PyQt5:",
        'technologies_used_five_card_one_content': "Used for creating the graphical user interface. The library's versatility allows for creating a modern, responsive UI.",
        'technologies_used_five_card_two': "- SQLite3:",
        'technologies_used_five_card_two_content': "A lightweight database engine embedded within the project. It is used to store and manage customer data, user credentials, and roles.",
        'technologies_used_five_card_three': "- Modular Structure:",
        'technologies_used_five_card_three_content': "The project is modular, with each functional area encapsulated in its own class. This design choice makes the project easier to maintain and extend.",
        'conclusion_content': "This project is a robust solution for managing customer information and user access within a business setting. It combines ease of use with essential security features, such as role-based access control and data validation. The project’s design and implementation demonstrate effective use of Python's capabilities for building desktop applications with an intuitive user interface and reliable data management."
    }
    return render(request, "projectIntroduction.html", context)







def mobileProjectsViews(request):
    projects = [
        # Plans App (IOS)
        {
            'name': 'Plans',
            'os': 'IOS',
            'os_color': 'iosColor',
            'os_icon': 'apple.svg',
            'technologies': [
                {'label': 'Language', 'value': 'Swift', 'icon': 'swift.png'},
                {'label': 'UI', 'value': 'Swift UI', 'icon': 'swiftui.png'},
                {'label': 'Database', 'value': 'Firebase', 'icon': 'firebase.svg'},
                {'label': 'Architecture', 'value': 'MVVM', 'icon': 'mvvm.png'},
            ],
            'description': 'Plans App simplifies task management to enhance organization and productivity.',
            'url_name': 'plans'
        },
        # Facetime (IOS)
        {
            'name': 'Facetime',
            'os': 'IOS',
            'os_color': 'iosColor',
            'os_icon': 'apple.svg',
            'technologies': [
                {'label': 'Language', 'value': 'Swift', 'icon': 'swift.png'},
                {'label': 'UI', 'value': 'UIkit', 'icon': 'uikit.svg'},
                {'label': 'Database', 'value': 'Firebase', 'icon': 'firebase.svg'},
                {'label': 'Stream', 'value': 'Getstream.io', 'icon': 'stream.png'},
            ],
            'description': 'FaceTime enables seamless, high-quality video and audio calls for effortless personal and professional communication.',
            'url_name': 'faceTime'
        },
        # Flutter Weather App (IOS)
        {
            'name': 'Weather App',
            'os': 'IOS',
            'os_color': 'iosColor',
            'os_icon': 'apple.svg',
            'technologies': [
                {'label': 'Language', 'value': 'Dart', 'icon': 'dart.png'}, # swift.png yerine dart.png kullanıldı
                {'label': 'UI, Framework', 'value': 'Flutter', 'icon': 'flutter-original.svg'},
                {'label': 'API', 'value': 'Openweather API', 'icon': 'openweatherapi.png'},
                {'label': 'Architecture', 'value': 'MVVM', 'icon': 'mvvm.png'},
            ],
            'description': 'My Weather App delivers real-time updates, accurate forecasts, and severe weather alerts to keep you informed and prepared.',
            'url_name': 'flutterWeatherApp'
        },
        # Notebook (ANDROID)
        {
            'name': 'Notebook',
            'os': 'ANDROID',
            'os_color': 'androidColor',
            'os_icon': 'android.png',
            'technologies': [
                {'label': 'Language', 'value': 'Kotlin', 'icon': 'kotlin.png'}, # swift.png yerine kotlin.png kullanıldı
                {'label': 'UI', 'value': 'Material Design 3', 'icon': 'materialdesign3.png'},
                {'label': 'Database', 'value': 'Room', 'icon': 'room.svg'},
                {'label': 'Framework', 'value': 'Compose', 'icon': 'compose.svg'},
                {'label': 'Architecture', 'value': 'MVVM', 'icon': 'mvvm.png'},
            ],
            'description': 'Notebook App offers a secure, user-friendly platform to capture notes, manage tasks, and enhance productivity on the go.',
            'url_name': 'notebook'
        },
        # Word Guess (ANDROID)
        {
            'name': 'Word Guess',
            'os': 'ANDROID',
            'os_color': 'androidColor',
            'os_icon': 'android.png',
            'technologies': [
                {'label': 'Language', 'value': 'Kotlin', 'icon': 'kotlin.png'}, # swift.png yerine kotlin.png kullanıldı
                {'label': 'UI', 'value': 'Material Design 3', 'icon': 'materialdesign3.png'},
                {'label': 'Database', 'value': 'Firebase', 'icon': 'firebase.svg'},
                {'label': 'Framework', 'value': 'Compose', 'icon': 'compose.svg'},
                {'label': 'Architecture', 'value': 'MVVM', 'icon': 'mvvm.png'},
            ],
            'description': 'WordGuess App offers an engaging platform to challenge vocabulary, improve language skills, and track progress through interactive puzzles and quizzes.',
            'url_name': 'wordGuess'
        },
        # Twitter Clone (ANDROID)
        {
            'name': 'Twitter Clone',
            'os': 'ANDROID',
            'os_color': 'androidColor',
            'os_icon': 'android.png',
            'technologies': [
                {'label': 'Language', 'value': 'Kotlin', 'icon': 'kotlin.png'}, # swift.png yerine kotlin.png kullanıldı
                {'label': 'UI', 'value': 'Material Design 3', 'icon': 'materialdesign3.png'},
                {'label': 'Database', 'value': 'Firebase', 'icon': 'firebase.svg'},
                {'label': 'Framework', 'value': 'Compose', 'icon': 'compose.svg'},
                {'label': 'Architecture', 'value': 'MVVM', 'icon': 'mvvm.png'},
            ],
            'description': 'Twitter Clone App is a user-friendly social platform for real-time updates, seamless engagement, and staying connected with global trends.',
            'url_name': 'twitterClone'
        },
        # Threads Clone (ANDROID)
        {
            'name': 'Threads Clone',
            'os': 'ANDROID',
            'os_color': 'androidColor',
            'os_icon': 'android.png',
            'technologies': [
                {'label': 'Language', 'value': 'Kotlin', 'icon': 'kotlin.png'}, # swift.png yerine kotlin.png kullanıldı
                {'label': 'UI', 'value': 'Material Design 3', 'icon': 'materialdesign3.png'},
                {'label': 'Database', 'value': 'Firebase', 'icon': 'firebase.svg'},
                {'label': 'Framework', 'value': 'Compose', 'icon': 'compose.svg'},
                {'label': 'Architecture', 'value': 'MVVM', 'icon': 'mvvm.png'},
            ],
            'description': 'Threads Clone App facilitates focused, threaded discussions for deeper engagement, knowledge sharing, and connection with like-minded individuals.',
            'url_name': 'threadsClone'
        },
        # Weather App (ANDROID)
        {
            'name': 'Weather App',
            'os': 'ANDROID',
            'os_color': 'androidColor',
            'os_icon': 'android.png',
            'technologies': [
                {'label': 'Language', 'value': 'Kotlin', 'icon': 'kotlin.png'}, # swift.png yerine kotlin.png kullanıldı
                {'label': 'UI', 'value': 'Material Design 3', 'icon': 'materialdesign3.png'},
                {'label': 'API', 'value': 'Accuweather API', 'icon': 'accuweatherapi.png'},
                {'label': 'Database', 'value': 'Firebase', 'icon': 'firebase.svg'},
                {'label': 'API Client', 'value': 'Retrofit', 'icon': 'retrofit.png'},
                {'label': 'Architecture', 'value': 'MVVM', 'icon': 'mvvm.png'},
            ],
            'description': 'Weather App provides accurate, real-time forecasts and detailed local weather insights for confident planning.',
            'url_name': 'weatherApp'
        },
        # Recipe (ANDROID)
        {
            'name': 'Recipe',
            'os': 'ANDROID',
            'os_color': 'androidColor',
            'os_icon': 'android.png',
            'technologies': [
                {'label': 'Language', 'value': 'Kotlin', 'icon': 'kotlin.png'}, # swift.png yerine kotlin.png kullanıldı
                {'label': 'UI', 'value': 'Material Design 3', 'icon': 'materialdesign3.png'},
                {'label': 'Database', 'value': 'SharedPreferences', 'icon': 'sharedpreferences.png'},
                {'label': 'Framework', 'value': 'Compose', 'icon': 'compose.svg'},
            ],
            'description': 'Recipe is your ultimate culinary companion, offering a vast collection of recipes with detailed instructions and tips for effortless meal planning and cooking inspiration.',
            'url_name': 'recipe'
        },
        # Voice Recorder (ANDROID)
        {
            'name': 'Voice Recorder',
            'os': 'ANDROID',
            'os_color': 'androidColor',
            'os_icon': 'android.png',
            'technologies': [
                {'label': 'Language', 'value': 'Kotlin', 'icon': 'kotlin.png'}, # swift.png yerine kotlin.png kullanıldı
                {'label': 'UI', 'value': 'Material Design 3', 'icon': 'materialdesign3.png'},
                {'label': 'Database', 'value': 'SharedPreferences', 'icon': 'sharedpreferences.png'},
                {'label': 'Framework', 'value': 'Compose', 'icon': 'compose.svg'},
            ],
            'description': 'SimpleVoice Recorder offers an easy-to-use interface for recording, playback, and organized tagging, ideal for notes, memos, and interviews.',
            'url_name': 'voiceRecorder'
        },
        # Wallet (ANDROID)
        {
            'name': 'Wallet',
            'os': 'ANDROID',
            'os_color': 'androidColor',
            'os_icon': 'android.png',
            'technologies': [
                {'label': 'Language', 'value': 'Kotlin', 'icon': 'kotlin.png'}, # swift.png yerine kotlin.png kullanıldı
                {'label': 'UI', 'value': 'Material Design 3', 'icon': 'materialdesign3.png'},
                {'label': 'Framework', 'value': 'Compose', 'icon': 'compose.svg'},
            ],
            'description': 'Wallet UI is a minimalist, design-focused app showcasing clean interface elements and straightforward navigation for an uncluttered user experience.',
            'url_name': 'walletUi'
        },
        # Rick and Morty (ANDROID)
        {
            'name': 'Rick and Morty',
            'os': 'ANDROID',
            'os_color': 'androidColor',
            'os_icon': 'android.png',
            'technologies': [
                {'label': 'Language', 'value': 'JavaScript', 'icon': 'javascript.png'},
                {'label': 'Language', 'value': 'TypeScript', 'icon': 'typescript.png'},
                {'label': 'UI', 'value': 'React Native', 'icon': 'react.svg'},
                {'label': 'API', 'value': 'RickAndMorty API', 'icon': 'rickandmortyapi.png'},
            ],
            'description': 'Rick and Morty Characters app offers a user-friendly interface to explore episodes and characters from the popular animated series, providing easy access to detailed insights and an engaging experience.',
            'url_name': 'rickAndMorty'
        },
        # QR Scanner (ANDROID)
        {
            'name': 'QR Scanner',
            'os': 'ANDROID',
            'os_color': 'androidColor',
            'os_icon': 'android.png',
            'technologies': [
                {'label': 'Language', 'value': 'Dart', 'icon': 'dart.png'},
                {'label': 'UI, Framework', 'value': 'Flutter', 'icon': 'flutter-original.svg'},
                {'label': 'IDE', 'value': 'Android Studio', 'icon': 'android.png'},
            ],
            'description': 'QR Scanner app provides a fast, reliable, and user-friendly way to scan QR codes, instantly accessing websites, product details, promotions, and more.',
            'url_name': 'qrScanner'
        }

        
    ]
    return render(request, 'mobileProjects.html', {'projects': projects})