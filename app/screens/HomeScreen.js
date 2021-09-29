import React from "react";
import { Button, View, Text } from "react-native";
import { Buttons } from "../styles";

const HomeScreen = ({ navigation }) => {
  return (
    <View style={{ flex: 1, alignItems: "center", justifyContent: "center" }}>
      <Text>Home Screen</Text>
      <Button
        title="Go to Map"
        onPress={() => navigation.navigate("Map")}
      />
      <Button
        title="Go to Settings"
        onPress={() => navigation.navigate("Settings")}
      />
    </View>
  );
};
export default HomeScreen;
