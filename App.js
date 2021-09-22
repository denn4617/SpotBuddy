import * as React from "react";
import { Text, View } from "react-native";
import { Ionicons } from "@expo/vector-icons";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import { NavigationContainer } from "@react-navigation/native";

import { Colors } from "./app/styles";
// få lige fikset ./screens/index.js så components kan importeres nemmere og pænere
import {
  HomeScreen,
  NotificationScreen,
  SettingsScreen,
  LoginScreen,
} from "./app/screens";

//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
//Ionicons - https://oblador.github.io/react-native-vector-icons/
//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

const Tab = createBottomTabNavigator();

export default function App() {
  return (
    <NavigationContainer style={Colors.background}>
      <Tab.Navigator
        screenOptions={({ route }) => ({
          tabBarIcon: ({ focused, color, size }) => {
            let iconName;

            switch (route.name) {
              case "Home":
                iconName = focused ? "ios-home" : "ios-home-outline";
                break;
              case "Notifications":
                iconName = focused
                  ? "ios-notifications-circle"
                  : "ios-notifications-circle-outline";
                break;
              case "Settings":
                iconName = focused ? "ios-settings" : "ios-settings-outline";
                break;
              case "Login":
                iconName = focused ? "ios-sad" : "ios-sad-outline";
                break;
              default:
                break;
            }

            // You can return any component that you like here!
            return <Ionicons name={iconName} size={size} color={color} />;
          },
        })}
        tabBarOptions={{
          activeTintColor: "green",
          inactiveTintColor: "gray",
        }}
      >
        <Tab.Screen name="Home" component={HomeScreen} />
        <Tab.Screen name="Notifications" component={NotificationScreen} />
        <Tab.Screen name="Settings" component={SettingsScreen} />
        <Tab.Screen name="Login" component={LoginScreen} />
      </Tab.Navigator>
    </NavigationContainer>
  );
}
