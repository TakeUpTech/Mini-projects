using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class Message : MonoBehaviour
{
    public TMP_InputField message;
    public GameObject messagePrefab;
    [SerializeField] List<string> messageList;
    Color myColor = new Color(252/255f, 187/255f, 109/255f);
    Color defaultColor = new Color(104/255f, 93/255f, 121/255f);
    private string data;
    private string separator = "__;__";
    private string subSeparator = "_;_";

    // Start is called before the first frame update
    void Start()
    {
        InstantiateMessage(messagePrefab, "Welcome! Ready to send what is important to you?", defaultColor, Color.white);
        InstantiateMessage(messagePrefab, "Press the top bar to display some previous messages according to your mood.", defaultColor, Color.white);

        data = "";
        if(PlayerPrefs.HasKey("messageData")){ // Removers saved data if it exist
            data = PlayerPrefs.GetString("messageData");
        }

        string[] messages = data.Split(separator); // Saved data containing is splitted according to a string separator
        for (int i = 0; i < messages.Length; i++)  // Each element correspond to a message and its associated mood
        {
            if(messages[i] != ""){
                messageList.Add(messages[i]); // Message and its mood are added in the message list
            }
        }
    }

    public void SendMessage(int mood){
        if(message.text != ""){ // Empty messages can't be sent
            messageList.Add(message.text + subSeparator + mood); // Message and its mood are added in the message list
            InstantiateMessage(messagePrefab, message.text, myColor, Color.black); // The message is creating on the UI of the application
            SaveMessage(message.text, mood); // The message sent is saved
            message.text = ""; // Input textfield is cleared
        }/* else{
            Debug.Log("No message to send.");
        } */
    }

    public void MemoryMessage(int mood){
        // Create a list of messages according to the selected mood. Those messages are part of the main message list
        List<string> moodFitList = new List<string>();
        for (int i = 0; i < messageList.Count; i++)
        {
            if(GetMood(messageList, i) == mood){
                moodFitList.Add(GetText(messageList, i));
            }
        }

        if(moodFitList.Count > 0){ // If it exist messages associated to the selected mood
            int index = Random.Range(0, moodFitList.Count); // We choose a message by its index form the list randomly

            /* Color color;
            if(mood == 5)
            {
                color = badColor;
            }else{
                color = goodColor;
            } */

            InstantiateMessage(messagePrefab, moodFitList[index], defaultColor, Color.white); // The message is creating on the UI of the application
        }
    }

    private string GetText(List<string> messageList, int index){
        return messageList[index].Split(subSeparator)[0];
    }

    private int GetMood(List<string> messageList, int index){
        return int.Parse(messageList[index].Split(subSeparator)[1]);
    }

    private void SaveMessage(string text, int mood){
        data += text + subSeparator + mood + separator; // Data is saved according to a specific pattern: Text_;_Mood__;__Text_;_Mood...
        PlayerPrefs.SetString("messageData", data); // String data is save into the register
    }

    public void ClearMessageList(){
        messageList.Clear(); // Empties the list of all its elements
    }

    private void InstantiateMessage(GameObject prefab, string text, Color backgroundColor, Color textColor){
        // Create a clone of message UI prefab on the UI application screen, its parent is the possessor of this script
        GameObject clone = Instantiate(prefab, this.transform); 
        clone.GetComponentInChildren<TextMeshProUGUI>().text = text; // The text of the message created is set
        clone.GetComponentInChildren<TextMeshProUGUI>().color = textColor; // The color of the text message created is set
        clone.GetComponent<Image>().color = backgroundColor; // The color of the message background created is set
    }
}
