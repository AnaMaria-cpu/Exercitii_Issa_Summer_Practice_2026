# . Fie functia build_xml_element care primeste urmatorii parametri:
# - tag,
# - content si
# - elemente cheie-valoare date ca parametri cu nume.
# Sa se construiasca si sa se returneze un string care reprezinta elementul XML aferent.
# Exemplu:
# build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
# => "<a href="http://python.org" class_="my-link” id="someid">Hello there</a>"


def build_xml_element(tag, content, **attributes):
    result = "<" + tag

    for key in attributes:
        xml_key = key

        if xml_key.startswith("_"):
            xml_key = xml_key[1:]

        result = result + " " + xml_key + '="' + str(attributes[key]) + '"'

    result = result + ">"
    result = result + content
    result = result + "</" + tag + ">"

    return result


print(
    build_xml_element(
        "a",
        "Hello there",
        href="http://python.org",
        _class="my-link",
        id="someid"
    )
)