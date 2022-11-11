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
    // Color goodColor = new Color(172/255f, 50/255f, 50/255f);
    // Color badColor = new Color(18/255f, 142/255f, 88/255f);
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
        if(PlayerPrefs.HasKey("messageData")){
            data = PlayerPrefs.GetString("messageData");
        }

        string[] messages = data.Split(separator);
        for (int i = 0; i < messages.Length; i++)
        {
            if(messages[i] != ""){
                messageList.Add(messages[i]);
            }
        }
    }

    public void SendMessage(int mood){
        if(message.text != ""){
            messageList.Add(message.text + subSeparator + mood);
            InstantiateMessage(messagePrefab, message.text, myColor, Color.black);
            SaveMessage(message.text, mood);
            message.text = "";
        }/* else{
            Debug.Log("No message to send.");
        } */
    }

    public void MemoryMessage(int mood){
        List<string> moodFitList = new List<string>();
        for (int i = 0; i < messageList.Count; i++)
        {
            if(GetMood(messageList, i) == mood){
                moodFitList.Add(GetText(messageList, i));
            }
        }

        if(moodFitList.Count > 0){
            int index = Random.Range(0, moodFitList.Count);

            /* Color color;
            if(mood == 5)
            {
                color = badColor;
            }else{
                color = goodColor;
            } */

            InstantiateMessage(messagePrefab, moodFitList[index], defaultColor, Color.white);
        }
    }

    private string GetText(List<string> messageList, int index){
        return messageList[index].Split(subSeparator)[0];
    }

    private int GetMood(List<string> messageList, int index){
        return int.Parse(messageList[index].Split(subSeparator)[1]);
    }

    private void SaveMessage(string text, int mood){
        data += text + subSeparator + mood + separator;
        PlayerPrefs.SetString("messageData", data);
    }

    public void ClearMessageList(){
        messageList.Clear();
    }

    private void InstantiateMessage(GameObject prefab, string text, Color backgroundColor, Color textColor){
        GameObject clone = Instantiate(prefab, this.transform);
        clone.GetComponentInChildren<TextMeshProUGUI>().text = text;
        clone.GetComponentInChildren<TextMeshProUGUI>().color = textColor;;
        clone.GetComponent<Image>().color = backgroundColor;
    }
}
