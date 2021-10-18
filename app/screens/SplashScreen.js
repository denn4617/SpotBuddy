// import React from "react";
// import { NavigationContainer } from "@react-navigation/native";
// import Navigation from "./Navigation";
// import { View, Image } from "react-native";
// import AsyncStorage from '@react-native-community/async-storage';
// import reduxStore from "./Utils/reduxConfig";

// const SplashScreen = (props) => {
//     useEffect(() => {
//         checkToken();
//     }, []);

//     const checkToken = async () => {
//         const token = await AsyncStorage.getItem("token");
//         const user = await AsyncStorage.getItem("user");
//         const userData = JSON.parse(user);
//         if (token != null) {
//             props.save_user(userData);
//         } else {
//             props.navigation.navigate("Login");
//         }
//     };

//     return (
//         <View style={styles.container}>
//             <Image
//                 source={require("../assets/splash.png")}
//                 style={styles.image}
//             />
//         </View>
//     );
// };
// export default SplashScreen;
