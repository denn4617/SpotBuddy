import React from "react";
import { View, TextInput, Button, Text, TouchableOpacity } from "react-native";
import { Colors, TextStyle } from "../styles/index";

const LoginScreen = ({ navigation }) => {
  return (
    <View style={{ flex: 1, alignItems: "center", justifyContent: "center" }}>
      <View style={TextStyle.loginTextInput}>
        <TextInput style={Colors.textInput} placeholder="Username or email" />
      </View>
      <View style={TextStyle.loginTextInput}>
        <TextInput style={Colors.textInput} placeholder="Password" />
      </View>
      <View
        style={{
          flexDirection: "row",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <TouchableOpacity>
          <Text
            style={{ fontSize: 18, fontWeight: "300" /*ændre fontWeight */ }}
          >
            Don't have an account?
          </Text>
        </TouchableOpacity>
        <Button
          title="Sign up"
          color="green"
          onPress={() => navigation.navigate("Settings")}
        />
        <Button title="Forgot Password">
          <TouchableOpacity>
            <Text style={{ color: "white", fontSize: 11 }}>
              Forgot Password?
            </Text>
          </TouchableOpacity>
        </Button>
      </View>
    </View>
  );
};
export default LoginScreen;
