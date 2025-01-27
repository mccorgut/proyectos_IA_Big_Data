from xml.etree import ElementTree

Victories = ElementTree.parse("victories.xml").getroot()

def main():
    user_action = "Paper"
    computer_action = "Rock"
    test_xpath = f"./victory[@choice='{user_action}'][@against='{computer_action}']"
    
    test_match = Victories.find(test_xpath)
    choice = test_match.attrib["choice"]
    against = test_match.attrib["against"]
    
    print(f"choice: {choice}")
    print(f"against: {against}")
    print(test_match.text.strip())

if __name__ == "__main__":
  main()

