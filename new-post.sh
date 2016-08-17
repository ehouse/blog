#!/bin/bash
case $1 in
    -h|--help)
        echo Usage: new-post.sh title
        exit
        ;;
esac

date=`date +%F`
title=$1
disksafetitle=$(echo $title | tr " " - | tr '[:upper:]' '[:lower:]')
htmlsafetitle=$(echo $title | perl -n -mHTML::Entities -e ' ; print HTML::Entities::encode_entities($_) ;')

cat > ./content/blog/"$disksafetitle".md <<endmsg
Title: $htmlsafetitle
Date: $date
Status: draft
Summary: Short version for index and feeds

This is the content of my super blog post.
endmsg

echo "File can be edited at $(pwd)/content/blog/$disksafetitle.md"
