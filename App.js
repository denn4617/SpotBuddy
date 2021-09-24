import * as React from "react";
import { Text, View } from "react-native";
import { Ionicons } from "@expo/vector-icons";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import { NavigationContainer } from "@react-navigation/native";

import { Colors } from "./app/styles";
// få lige fikset ./screens/index.js så components kan importeres nemmere og pænere
import {
  HomeScreen,
  MapScreen,
  SettingsScreen,
  LoginScreen,
} from "./app/screens";

//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
// Ionicons - https://oblador.github.io/react-native-vector-icons/ //
//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

const Tab = createBottomTabNavigator();

export default function App() {
  return (
    <NavigationContainer style={Colors.background}>
      <Tab.Navigator
        screenOptions={({ route }) => ({
          tabBarIcon: ({ focused, color, size }) => {
            let iconName;
            let iconSize;

            switch (route.name) {
              case "Home":
                iconName = focused ? "home" : "home-outline";
                size = focused ? 30 : size;
                break;
              case "Map":
                iconName = focused
                  ? "location"
                  : "location-outline";
                  size = focused ? 30 : size;
                break;
              case "Settings":
                iconName = focused ? "settings" : "settings-outline";
                size = focused ? 30 : size;
                break;
              case "Login":
                iconName = focused ? "sad" : "sad-outline";
                size = focused ? 30 : size;
                break;
              default:
                break;
            }

            // You can return any component that you like here!
            return <Ionicons name={iconName} size={size} color={color} />;
          },
        })}
        tabBarOptions={{
          activeTintColor: "white",
          inactiveTintColor: "white",
          allowFontScaling: true,
          style: {
            backgroundColor: "green",
          },
        }}
      >
        <Tab.Screen name="Home" component={HomeScreen} />
        <Tab.Screen name="Map" component={MapScreen} />
        <Tab.Screen name="Settings" component={SettingsScreen} />
        <Tab.Screen name="Login" component={LoginScreen} />
      </Tab.Navigator>
    </NavigationContainer>
  );
}
